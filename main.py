import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = pd.read_csv("data.csv", header=None)
names = pd.read_csv("names.csv", header=None)

def calculate_loss(partition, objective):
	def compare_pair(pair):
		ans = False
		for part in partition:
			return ans or (pair[0] in part and pair[1] in part)
	total = ()			# find all the 
	loss = 0
	for part in partition:
		total += part
	every_pair = itertools.combinations(total, 2)
	for pair in every_pair:
		loss += objective(pair, compare_pair(pair))
	return loss

calculate_loss()