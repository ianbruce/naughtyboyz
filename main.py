import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = pd.read_csv("data.csv", header=None)
names = pd.read_csv("names.csv", header=None)

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
		total += part
	every_pair = itertools.combinations(total, 2)
	for pair in every_pair:
		loss += objective(pair, compare_pair(pair))
	return loss