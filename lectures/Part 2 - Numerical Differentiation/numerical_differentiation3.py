# we can solve ordinary differential equations using finite difference methods
# e.g., Euler's method estimates the next point in a curve from the local first derivative
# (first-order Taylor series approximation)
def euler(y0, dydx, dx):
	return y0 + dydx*dx

# example: radioactive decay, a first-order ODE
# at time t, the rate of change of the number of radioactive atoms with half-life t_half in a sample is proportional to the current number of atoms
# dN/dt = -lambda * N(t)
# where lambda is the decay constant, lambda = ln(2)/t_half

import math

N0 = 500 # atoms
t_half = 1 # hour
decay_const = math.log(2) / t_half # math.log is the natural logarithm

dt = 0.1 # time interval in hours
times = [i*dt for i in range(50)] # hours
N = [] # atoms

N_t = N0 # initialize N
for t in times:
	N_t = euler(N_t, -decay_const*N_t, dt)
	N.append(N_t)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(times, N)
plt.show()