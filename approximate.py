import numpy as np
import itertools
import pandas as pd
import networkx as nx

def rand_affinity(n, probs):
	return np.random.choice([-1,0,1], (n,n), p=probs)

mat = rand_affinity(200, [.1, .7, .2])
np.savetxt("test_mat.csv", mat, delimiter=",")

# In this algorithm, we will represent partitions as incidence vectors, with 1
# at position i representing scout i being in the partition, and 0 representing
# them not being in the partition
def compute_sol(matrix):

	# This function expects 1's at incidences of scouts being in the first partition,
	# 2's where scouts are in the second, and 0's otherwise
	def optimize_pair(part):
		G = 1
		Ds = [[diff(i, part) for i in range(len(part))] for j in range(1,3)] # Computes D's
		
	# i - the index of the scout in question
	# part - the partition scout i is a member of
	def external(i, part):
		sum = 0
		for j in range(len(part)):
			sum += matrix[i, j] if part[j] == 2 else 0
		return sum

	# i - the index of the scout in question
	# part - the partition scout i is a member of
	def internal(i, part):
		sum = 0
		for j in range(len(part)):
			sum += matrix[i, j] if part[j] == 1 else 0
		return sum

	# difference between external and internal costs for the
	def diff(i, part):
		return external(i, part) - internal(i, part)

	def gain(d1, d2, i, j):
		return d1 + d2 - matrix[i,j]

	def update_ext():
		pass

	def swap_cost(a, b):
		pass


	return optimize_pair([i for i in itertools.chain(itertools.repeat(1, 100), itertools.repeat(2, 100))])


