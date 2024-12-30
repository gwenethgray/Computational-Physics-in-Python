# you can use random sampling to approximate an area
# this is Monte Carlo integration

# rejection method to approximate the area under a curve f(x):
#   initialize counter to 0
#   sample N random number pairs Rx, Ry in a 2D window
#   for each pair, if Ry < f(Rx), increment counter by 1
#   fraction of points under the curve = counter / N
#   area under curve = fraction under curve * area of box

# the same technique can be used to approximate pi
# pi = ratio of area of circle of radius r to square of side length 2r
# check if a point (Rx,Ry) is in the circle by the equation:
# Rx**2 + Ry**2 < r**2

from rng import MCG
rng = MCG()

r = 1 # radius of circle
x0, y0 = 1, 1 # center of circle
A = (2*r)**2 # area of box

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# draw circle
circle = plt.Circle((x0, y0), r, fill=False)
ax.add_patch(circle)
ax.set_xlim(0, 2*r)
ax.set_ylim(0, 2*r)

N = 100000
random_numbers_x = [R/rng.modulus for R in rng.sampleN(N)]
random_numbers_y = [R/rng.modulus for R in rng.sampleN(N)]

in_circle_x = []
in_circle_y = []
not_in_circle_x = []
not_in_circle_y = []

import math

for i in range(N):
	Rx = random_numbers_x[i]
	Ry = random_numbers_y[i]
	x = 2*r*Rx
	y = 2*r*Ry
	if math.hypot(1 - x, 1 - y) < r**2:
		in_circle_x.append(x)
		in_circle_y.append(y)
	else:
		not_in_circle_x.append(x)
		not_in_circle_y.append(y)

print(f"Pi = {A*len(in_circle_x)/N}")

plt.scatter(in_circle_x, in_circle_y, color="blue")
plt.scatter(not_in_circle_x, not_in_circle_y, color="red")

plt.show()