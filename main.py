import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", header=None, dtype='float')
data = data.fillna(float('-inf'))
names = pd.read_csv("names.csv", header=None)

def min_cut(x, y, partition):
	for patrol in partition:
		if (x in patrol and not y in patrol) \
		or (y in patrol and not x in patrol):
			return data[x][y] + data[y][x]
		else:
			return 0
