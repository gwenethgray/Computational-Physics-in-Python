# conservation of linear momentum in 2D
# reflective boundary conditions - particles collide with walls

import math

class Particle:
	def __init__(self, particle_id, m, r, x, y, vx, vy):
		self.id = particle_id # integer
		self.m = m # mass
		self.r = r # radius
		self.x = x # x-component of position
		self.y = y # y-component of position
		self.vx = vx # x-component of velocity
		self.vy = vy # y-component of velocity

	# solve equations of motion after a time interval dt
	# reflective boundary conditions
	def euler(self, fx, fy, dt):
	    # update velocity from force
	    self.vx += (fx / self.m) * dt
	    self.vy += (fy / self.m) * dt

	    # predict new position
	    x_new = self.x + self.vx * dt
	    y_new = self.y + self.vy * dt

	    # reflect at x=0 or x=L
	    if x_new < 0:
	        x_new = -x_new
	        self.vx = -self.vx
	    elif x_new > L:
	        x_new = 2*L - x_new
	        self.vx = -self.vx

	    # reflect at y=0 or y=L
	    if y_new < 0:
	        y_new = -y_new
	        self.vy = -self.vy
	    elif y_new > L:
	        y_new = 2*L - y_new
	        self.vy = -self.vy

	    # update position
	    self.x = x_new
	    self.y = y_new

	# check whether this particle overlaps with another particle with radius r1 at (x1,y1)
	def check_overlap(self, p1):
		return math.hypot(p1.x - self.x, p1.y - self.y) < self.r + p1.r

	# change velocities of overlapping particles
	def change_velocities(self, p1):
		dx = p1.x - self.x
		dy = p1.y - self.y
		dist = math.hypot(dx, dy)
		# unit collision normal
		nx = dx / dist
		ny = dy / dist
		# velocity components along collision normal
		vn = self.vx*nx + self.vy*ny
		vn1 = p1.vx*nx + p1.vy*ny
		# apply 1D elastic collision rules to normal components
		vn_final = ((self.m - p1.m)*vn + 2*p1.m*vn1) / (self.m + p1.m)
		vn1_final = ((p1.m - self.m)*vn1 + 2*self.m*vn) / (self.m + p1.m)
		# convert back into vx, vy
		dvn = vn_final - vn
		dvn1 = vn1_final - vn1
		self.vx += dvn*nx
		self.vy += dvn*ny
		p1.vx += dvn1*nx
		p1.vy += dvn1*ny

from rng import MCG
rng = MCG()

# side length of square box environment
L = 10 # m

mass = 0.01 # kg
radius = 0.05 # m
vmax = 5 # m/s
fx, fy = 0, 0 # kg m/s^2
dt = 0.01 # s

N_particles = 20
# place the particles
particles = []
while len(particles) < N_particles:
	p = Particle(
		particle_id=len(particles),
		m=mass,
		r=radius,
		x=L*rng.sample()/rng.modulus,
		y=L*rng.sample()/rng.modulus,
		vx=vmax*(2*rng.sample() - 1)/rng.modulus,
		vy=vmax*(2*rng.sample() - 1)/rng.modulus)
	for p1 in particles:
		if p.check_overlap(p1):
			break
	particles.append(p)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

posns = ax.scatter([p.x for p in particles], [p.y for p in particles], s=radius*1000)

def animate(i):
	for p in particles:
		# advance particle
		p.euler(fx, fy, dt)
		for p1 in particles:
			# skip this particle itself
			if p1.id != p.id:
				if p.check_overlap(p1):
					# change both particles' velocities according to conservation of linear momentum
					p.change_velocities(p1)
	new_posns = np.c_[[p.x for p in particles], [p.y for p in particles]]
	posns.set_offsets(new_posns)
	return [posns]

ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

plt.show()