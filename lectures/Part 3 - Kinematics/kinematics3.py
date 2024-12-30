# trajectory of a projectile

class Particle:
	def __init__(self, m, x, y, vx, vy):
		self.m = m # mass
		self.x = x # x-component of position
		self.y = y # y-component of position
		self.vx = vx # x-component of speed
		self.vy = vy # y-component of speed

	# solve equations of motion after a time interval dt
	def euler(self, fx, fy, dt):
		self.x = self.x + self.vx*dt
		self.y = self.y + self.vy*dt
		self.vx = self.vx + (fx/self.m)*dt
		self.vy = self.vy + (fy/self.m)*dt

from math import cos, sin, pi

mass = 0.01 # kg
g = 9.8 # m/s^2
gforce = -g*mass # kg m/s^2
x0 = 0.01 # m
y0 = 0.01 # m
v0 = 15 # m/s
dt = 0.1 # s

# force of drag is linearly proportional to velocity with parameter k
# Fd = kv
# k is related to the terminal velocity vt of the falling object, which is reached when Fd = Fg
# k*vt = m*g --> k = m*g/vt
vt = 30 # m/s
k = mass*g/vt
dragforce = lambda v: k*v # can be used with vx or vy

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for theta0 in [43 + i for i in range(5)]:
	x = [x0]
	y = [y0]
	vx0 = v0 * cos(theta0*pi/180) # m/s
	vy0 = v0 * sin(theta0*pi/180) # m/s
	p = Particle(m=mass, x=x0, y=y0, vx=vx0, vy=vy0)
	while p.y > 0:
		fx = dragforce(abs(p.vx))
		fy = gforce + dragforce(abs(p.vy))
		p.euler(fx, fy, dt)
		x.append(p.x)
		y.append(p.y)
	line, = ax.plot(x, y, label=f"{theta0} degrees")

ax.set_ylim(0, 10)
plt.title("Parabolic Motion of a Projectile")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid()
plt.legend()
plt.savefig("projectile_motion.png", dpi=100)
plt.show()