import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = pd.read_csv("data.csv", header=None, dtype='float')
data = data.fillna(float('-inf'))
names = pd.read_csv("names.csv", header=None)

def min_cut(pair, in_same_patrol):
	x, y = pair
	if not in_same_patrol:
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

def brute_force_solver(d=data, num_patrols=2, min_patrol_size=6, max_patrol_size=7):
	partitions = generate_partitions([], num_patrols, len(d))
	best_partition_so_far = None
	best_loss = float('inf')
	for part in partitions:
		if sum(part) >= min_patrol_size and sum(part) <= max_patrol_size:
			patrols = [[] for i in range(num_patrols)]
			for i in range(len(part)):
				patrols[part[i]] += [i]
			loss = calculate_loss(patrols, min_cut)	
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

best_patrol, best_loss = brute_force_solver()
print "Best patrol:", best_patrol
print "Loss:", best_loss
