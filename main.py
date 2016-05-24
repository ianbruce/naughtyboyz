from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = pd.read_csv("data.csv", header=None, dtype='float')
data = data.fillna(float('-inf'))
names = pd.read_csv("names.csv", header=None)

'''
Traditional Min Graph Cut

Change in loss function for scouts in *different* patrols

mutual friends: +2
one like, one indifferent: +1
one like, one dislike: 0
one dislike, one indifferent: -1 
mutual enmity: -2
'''
def min_cut(pair, in_same_patrol):
	x, y = pair
	if not in_same_patrol:
		return max(-2, data[x][y] + data[y][x])
	else:
		return 0

'''
Friendly Cut: maximize friendship within patrol

Change in loss function for scouts in *same* patrol:

mutual friends: -2
one like, one indifferent: -1
one like, one dislike: 0
one dislike, one indifferent: 0 
mutual enmity: 0
'''
def friendly_cut(pair, in_same_patrol):
	x, y = pair
	if in_same_patrol:
		return -1.0 * max(0, data[x][y] + data[y][x])
	else:
		return 0

'''
Enemy Cut: minimize enemies within patrol

Change in loss function for scouts in *same* patrol:

mutual friends:0 
one like, one indifferent: 0
one like, one dislike: 0
one dislike, one indifferent: +1 
mutual enmity: +2 
'''
def enemy_cut(pair, in_same_patrol):
	x, y = pair
	if in_same_patrol:
		return max(0, -(data[x][y] + data[y][x]))
	else:
		return 0

'''
Awkward Cut: same as Min Cut but with additional penalty
for one like, one dislike in same patrol

Change in loss function:

mutual friends: +2
one like, one indifferent: +1
one like, one dislike (same patrol): -1
one like, one dislike (different patrol): 0
one dislike, one indifferent: -1 
mutual enmity: -2
'''
def awkward_cut(pair, in_same_patrol):
	x, y = pair
	if in_same_patrol and data[x][y] == -data[y][x] and abs(data[x][y]) > 0:
		return -1
	elif not in_same_patrol:
		return max(-2, data[x][y] + data[y][x])
	else:
		return 0

# this function assumes that the partitions are disjoint, no
# check for this has been implemented
def calculate_loss(partition, objective):
	def compare_pair(pair): # returns true if pair is in the same partition,
		ans = False         # false otherwise
		for part in partition:
			ans = ans or (pair[0] in part and pair[1] in part)
		return ans
	total = ()			# total will include every element in the
	loss = 0			# partitions
	for part in partition:
		total += tuple(part)
	every_pair = itertools.combinations(total, 2)
	for pair in every_pair:
		loss += objective(pair, compare_pair(pair))
	return loss

def brute_force_solver(d=data, num_patrols=2, objective=min_cut, min_patrol_size=6, max_patrol_size=7):
	partitions = generate_partitions([], num_patrols, len(d))
	best_partition_so_far = None
	best_loss = float('inf')
	for part in partitions:
		if sum(part) >= min_patrol_size and sum(part) <= max_patrol_size:
			patrols = [[] for i in range(num_patrols)]
			for i in range(len(part)):
				patrols[part[i]] += [i]
			loss = calculate_loss(patrols, objective)	
			if loss < best_loss:
				best_partition_so_far = patrols
				best_loss = loss
	return best_partition_so_far, best_loss

def generate_partitions(arr, patrols, num_scouts):
	result = []
	if num_scouts == 0:
		return [arr]
	else:
		for i in range(patrols):
			for c in generate_partitions(arr + [i], patrols, num_scouts - 1):
				result += [c]
	return result
'''
Example use

best_patrol, best_loss = brute_force_solver()
print "Best patrol:", best_patrol
print "Loss:", best_loss
'''
