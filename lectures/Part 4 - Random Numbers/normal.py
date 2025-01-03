# Box-Muller method of sampling random numbers with a normal (Gaussian) distribution

from rng import MCG
import math

class Normal:
	def __init__(self, mean=0, std=1):
		self.mean = mean
		self.std = std
		self.rng = MCG()
		self.extra = None # store an unused normally-distributed variable

	def sample(self):
		# pick 2 uniform random numbers in the square extending from -1 to +1 in each direction (Numerical Recipes in C, pp217)
		if self.extra is not None:
			# retrieve a pre-computed Gaussian number
			v = self.extra
			self.extra = None
			return v
		else:
			R = 1 # distance to origin
			while R >= 1:
				v1 = self.rng.sample(-1,1) # x-coordinate
				v2 = self.rng.sample(-1,1) # y-coordinate
				R = v1*v1 + v2*v2 # is (v1,v2) inside the unit circle?

			box_muller_factor = self.std * math.sqrt(-2.0*math.log(R)/R)
			self.extra = self.mean + v1 * box_muller_factor
			return self.mean + v2 * box_muller_factor

	def sampleN(self, N):
		random_numbers = []
		for _ in range(N):
			random_numbers.append(self.sample())
		return random_numbers

if __name__ == '__main__':
	import matplotlib.pyplot as plt

	fig, ax = plt.subplots()

	for (mean, std) in [(0,1), (4,1), (10,3)]:
		nrm = Normal(mean, std)
		random_numbers = nrm.sampleN(100000)
		ax.hist(random_numbers, bins=30, alpha=0.6, label=f"Mean={mean},Sig={std}")

	plt.xlabel("Random Number")
	plt.ylabel("Frequency")
	plt.title("Box-Muller Gaussian Random Numbers")
	plt.legend()
	plt.show()