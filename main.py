import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = pd.read_csv("data.csv", header=None, dtype='float')
data = data.fillna(float('-inf'))
names = pd.read_csv("names.csv", header=None)

def min_cut(pair, in_same_patrol):
	x, y = pair
	if in_same_patrol:
		return data[x][y] + data[y][x]
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
	total = ()
	loss = 0
	for part in partition:
		total += part
	every_pair = itertools.combinations(total, 2)
	for pair in every_pair:
		loss += objective(pair, compare_pair(pair))
	return loss

def brute_force_solver(d=data, num_patrols=2):
	pass
