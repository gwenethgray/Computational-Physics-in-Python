# motion with periodic boundary conditions

L = 4.0 # length of window
mass = 0.01 # kg
dt = 0.1 # s
F0 = 0.0 # m/s^2: no acceleration in any direction

class Particle:
	def __init__(self, m, x, y, v):
		self.m = m # mass
		self.x = x # position
		self.y = y # position
		self.v = v # speed (only in x-direction)

	# solve equations of motion after a time interval dt
	def euler(self, force, dt):
		self.v = self.v + (force/self.m)*dt
		self.x = self.x + self.v*dt
		# right periodic BC
		if self.x > L:
			self.x = 0 + (self.x - L)
		elif self.x < 0:
			self.x = L - self.x


p1 = Particle(m=mass, x=L/3, y=3, v=0.5) # heading right
p2 = Particle(m=mass, x=L/3, y=2, v=-0.5) # heading left
p3 = Particle(m=mass, x=L/3, y=1, v=1.5) # heading right (fast!)
particles = [p1, p2, p3]

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim(0, L)
ax.set_ylim(0, 4)

posns = ax.scatter([p.x for p in particles], [p.y for p in particles], s=500)

def animate(i):
	# advance particles
	for p in particles:
		p.euler(F0, dt)
	new_posns = np.c_[[p.x for p in particles], [p.y for p in particles]]
	posns.set_offsets(new_posns)
	return [posns]

ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

plt.title("1D Motion with Periodic Boundary Conditions")
plt.xlabel("X (m)")
plt.show()