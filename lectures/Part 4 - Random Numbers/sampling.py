# sampling random numbers from a distribution that is not uniform

# if you know the probability density function (PDF), and can calculate the cumulative density function (CDF), then you can sample a number from the PDF by plugging a uniform random number into the CDF

from rng import MCG
rng = MCG()

# for example, take an exponential distribution with mean = 1 / mu:
#   pdf(x) = mu*exp(-mu*x)

# the CDF is the integral of pdf(x):
#   CDF(x) = 1 - exp(-mu*x)

# the CDF takes a value between 0 and 1, so uniformly sample a number R between 0 and 1 and set that number equal to the CDF, then solve for x
#   x = -mu*log(1 - R)

from math import exp, log

mu = 1
N = 1000

random_numbers = [R/rng.modulus for R in rng.sampleN(N)]
exp_numbers = [-mu*log(1 - R) for R in random_numbers]

import matplotlib.pyplot as plt

plt.figure()
plt.hist(exp_numbers, bins=20)
plt.show()