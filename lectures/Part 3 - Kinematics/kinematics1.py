# equations of motion are a second-order problem because we have to compute acceleration

# example 1: free fall due to gravity
# v(t) = dy/dt
# a(t) = dv/dt = F(t)/m

class Particle:
	def __init__(self, m, y, v):
		self.m = m # mass
		self.y = y # position
		self.v = v # speed

	# solve equations of motion after a time interval dt
	def euler(self, force, dt):
		self.y = self.y + self.v*dt
		self.v = self.v + (force/self.m)*dt

mass = 0.01 # kg
g = 9.8 # m/s^2
gforce = -g*mass # kg m/s^2
y0 = 100 # m
v0 = 0 # m/s
dt = 0.5 # s

p = Particle(m=mass, y=y0, v=v0)

y = [y0]
t = [0]

while p.y > 0:
	fy = gforce # constant for now
	p.euler(fy, dt)
	y.append(p.y)
	t.append(t[-1] + dt) # [-1] accesses last element in sequence

import matplotlib.pyplot as plt

plt.figure()
plt.plot(t, y)
plt.title("Free Fall due to Gravity")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.savefig("freefall.png", dpi=100)
plt.show()