# "random number generators" (RNG) are not truly random, only pseudo-random

# congruential generators are a class of RNG that use modular arithmetic with extremely large numbers to generate sequences of numbers that are so long (and sufficiently uniformly distributed) that they might as well be random
# simplest is the multiplicative congruential generator (MCG):
# X_k+1 = (a * X_k) % m
# X_0 = seed
# m = modulus, a very large prime number or power of a prime number
# a = multiplier, a number less than m that is still very large

# default parameters recommended by Stephen K. Park and Keith W. Miller
modulus = 2**31 - 1
initial_seed = int(modulus / 2)
multiplier = 7**5

class MCG:
	def __init__(self, seed=initial_seed, modulus=modulus, multiplier=multiplier):
		self.seed = seed
		self.modulus = modulus
		self.multiplier = multiplier
		self.last_number = (multiplier * seed) % modulus
		self.sequence = [] # collect the random numbers for repeatability

	def sample(self, low=0, high=modulus):
		R = (self.multiplier * self.last_number) % modulus # 0 <= R < modulus
		self.last_number = R
		self.sequence.append(R)
		# scale to lower and upper sampling limits
		R = low + (high - low)*(R / self.modulus)
		return R

	def sampleN(self, N, low=0, high=modulus):
		# sample N numbers
		numbers = []
		for i in range(N):
			numbers.append(self.sample(low, high))
		return numbers


if __name__ == '__main__':
	rng = MCG()

	# check uniformity of distribution
	N = 10000
	random_numbers = [R/rng.modulus for R in rng.sampleN(N)]

	import matplotlib.pyplot as plt

	plt.figure()
	plt.hist(random_numbers, bins=20)
	plt.hlines(N/20, 0, 1, ls="--", color="black", zorder=10)
	plt.show()