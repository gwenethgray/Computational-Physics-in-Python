# waves on a string

# using numpy instead of math because it has convenient 
import numpy as np

# length of string
L = 1.0 # cm
# wave speed
c = 1.0 # cm / s
# number of points on string
N = 100
# spacing of points
dx = L / (N - 1)
# timestep
dt = 0.009 # seconds
	# aside on "numerical stability":
	#   Courant-Friedrichs-Lewy condition is: c * dt / dx <= 1
	#
	# if cdt/dx > 1, the numerical solution (height) of the wave equation will blow up very quickly because floating-point round-off errors are amplified.
	# if cdt/dx = 1, the system is only "marginally stable" and the amplitude will still be greater than expected.
# total simulation time
tsim = 1.0 # seconds
# number of iterations of simulation
nsteps = int(tsim / dt)

# harmonic mode number
n = 2 # or 1, 3, 4, 5...

# initial positions
x = np.linspace(0, L, N) # N elements spaced dx apart
u_curr = np.sin(n * np.pi * x / L) # an element for each element in x
u_prev = np.zeros(N) # holds the previous state

import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
line, = ax.plot(x, u_curr)

ax.set_xlim(0, L)
ax.set_ylim(-35, 35)

def update(frame):
	global u_curr, u_prev

	u_next = np.zeros(N)

	for i in range(1, N - 1):
		# apply wave equation to each point on string
		u_next[i] = (
			2.0 * u_curr[i]
			- u_prev[i]
			+ (c * dt / dx)**2 * (u_curr[i+1] - 2.0*u_curr[i] + u_curr[i-1]))

	# enforce fixed boundary conditions
	u_next[0] = 0.0
	u_next[-1] = 0.0

	# shift states
	u_prev = u_curr
	u_curr = u_next

	# update plot
	line.set_ydata(u_curr)
	return line,

# animate
ani = animation.FuncAnimation(fig, update, frames=nsteps, interval=20)
plt.show()