# generating data for a simulation, writing it to a file, and then reading that file to plot the data

class Particle:
	def __init__(self, m, y, v):
		self.m = m # mass
		self.y = y # position
		self.v = v # speed

	# solve equations of motion after a time interval dt
	def euler(self, force, dt):
		self.v = self.v + (force/self.m)*dt
		self.y = self.y + self.v*dt

mass = 0.01 # kg
g = 9.8 # m/s^2
gforce = -g*mass # kg m/s^2
y0 = 100 # m
v0 = 0 # m/s
dt = 0.5 # s
t = [0]

p = Particle(m=mass, y=y0, v=v0)

f = open("freefall_data.csv", "w")
f.write("t,y\n") # header with newline character \n

while p.y > 0:
	f.write(f"{t[-1]},{p.y}\n") # write current time and position
	fy = gforce # constant
	p.euler(fy, dt)
	t.append(t[-1] + dt)

f.close()