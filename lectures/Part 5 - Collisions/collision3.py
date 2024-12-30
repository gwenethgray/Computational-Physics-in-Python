# what if energy and momentum are not conserved?
# when a particle collides with a wall, it loses some energy (thermal walls)
# this will show us thermalization as the system approaches an equilibrium temperature
# the energy loss will be sampled using the Maxwell-Boltzmann distribution

import math, random
# using the standard random package because sampling from the normal distribution is non-trivial

# sample two velocity components from the Maxwell-Boltzmann distribution at temperature T_wall
def sample_Maxwell_Boltzmann(m, T_wall, kB=1.0):
	# let Boltzmann constant be unity
	# velocity components are drawn from a normal distribution with mean = zero and variance = kB*T_wall/m
	sigma = math.sqrt(kB * T_wall / m)
	vx = random.gauss(0, sigma)
	vy = random.gauss(0, sigma)
	return vx, vy

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
	def euler(self, fx, fy, dt, T_wall):
	    # update velocity from force
	    self.vx += (fx / self.m) * dt
	    self.vy += (fy / self.m) * dt

	    # predict new position
	    x_new = self.x + self.vx * dt
	    y_new = self.y + self.vy * dt

	    # left wall collision
	    if x_new < 0:
	        # pin the particle to x=0
	        x_new = 0
	        # re-sample velocity from MB distribution
	        vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        # ensure vx_new > 0 so it goes back inside the box
	        while vx_new <= 0:
	            vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        self.vx, self.vy = vx_new, vy_new

	    # right wall collision
	    if x_new > L:
	        # pin the particle to x=L
	        x_new = L
	        # re-sample velocity from MB distribution
	        vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        # ensure vx_new < L so it goes back inside the box
	        while vx_new >= 0:
	            vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        self.vx, self.vy = vx_new, vy_new

	    # bottom wall collision
	    if y_new < 0:
	        # pin the particle to y=0
	        y_new = 0
	        # re-sample velocity from MB distribution
	        vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        # ensure vy_new > 0 so it goes back inside the box
	        while vy_new <= 0:
	            vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        self.vx, self.vy = vx_new, vy_new

	    # top wall collision
	    if y_new > L:
	        # pin the particle to y=L
	        y_new = L
	        # re-sample velocity from MB distribution
	        vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        # ensure vx_new > 0 so it goes back inside the box
	        while vy_new >= 0:
	            vx_new, vy_new = sample_Maxwell_Boltzmann(self.m, T_wall)
	        self.vx, self.vy = vx_new, vy_new

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
		if dist < 1e-12:
			# nudge particles apart slightly
			theta = 2*math.pi*rng.sample()/rng.modulus
			dx = 1e-5 * math.cos(theta)
			dy = 1e-5 * math.sin(theta)
			p1.x += dx
			p1.y += dy
			dist = math.hypot(p1.x - self.x, p1.y - self.y)
			if dist == 0:
				# highly unlikely, but just skip if in same position
				return

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
vmax = 1 # m/s
fx, fy = 0, 0 # kg m/s^2
dt = 0.01 # s
T_wall = 300 # Kelvin

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
		p.euler(fx, fy, dt, T_wall)
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