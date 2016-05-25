import numpy as np

def rand_affinity(n, probs):
	return np.random.choice([-1,0,1], (n,n), p=probs)

print(rand_affinity(10, [.1, .7, .2]))