# example 2: free fall due to gravity with air resistance
# v(t) = dy/dt
# a(t) = dv/dt = F(t)/m

mass = 0.01 # kg
g = 9.8 # m/s^2
gforce = -g*mass # kg m/s^2
y0 = 100 # m
v0 = 0 # m/s
dt = 0.1 # s

# force of drag is linearly proportional to velocity with parameter k
# Fd = kv
# k is related to the terminal velocity vt of the falling object, which is reached when Fd = Fg
# k*vt = m*g --> k = m*g/vt
vt = 30 # m/s
k = mass*g/vt
dragforce = lambda v: k*v # anonymous function

class Particle:
	def __init__(self, m, y, v):
		self.m = m # mass
		self.y = y # position
		self.v = v # speed

	# solve equations of motion after a time interval dt
	def euler(self, force, dt):
		self.y = self.y + self.v*dt
		self.v = self.v + (force/self.m)*dt


p1 = Particle(m=mass, y=y0, v=v0) # this one will feel drag
p2 = Particle(m=mass, y=y0, v=v0) # just gravity

y1 = [y0]
y2 = [y0]
t = [0]

while p2.y > 0:
	fy1 = gforce + dragforce(abs(p1.v))
	fy2 = gforce
	p1.euler(fy1, dt)
	p2.euler(fy2, dt)
	y1.append(p1.y)
	y2.append(p2.y)
	t.append(t[-1] + dt) # [-1] accesses last element in sequence

import matplotlib.pyplot as plt

plt.figure()
plt.plot(t, y1, label="Gravity+Drag")
plt.plot(t, y2, label="Gravity")
plt.title("Free Fall: Gravity and Air Resistance")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.legend()
plt.savefig("freefall_drag.png", dpi=100)
plt.show()