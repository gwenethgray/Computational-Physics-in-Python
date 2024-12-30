# other finite difference methods

# finite difference method - forward difference
# @params:
#   func: a continuous function of one variable x
#   a: the value of x at which to compute the derivative
#   dx: the magnitude of finite difference over which the change in the function is calculated
def forward_fd(func, a, dx):
	dy = func(a + dx) - func(a)
	return dy / dx

# finite difference method - backward difference
# @params:
#   func: a continuous function of one variable x
#   a: the value of x at which to compute the derivative
#   dx: the magnitude of finite difference over which the change in the function is calculated
def backward_fd(func, a, dx):
	dy = func(a) - func(a - dx)
	return dy / dx

# finite difference method - central difference
# @params:
#   func: a continuous function of one variable x
#   a: the value of x at which to compute the derivative
#   dx: the magnitude of finite difference over which the change in the function is calculated
def central_fd(func, a, dx):
	dy = func(a + dx) - func(a - dx)
	return dy / (2*dx)

def square(x):
	return (x - 2)**2 + 2

from math import sin
import matplotlib.pyplot as plt

x = [i*0.1 for i in range(65)]
y0 = [square(a) for a in x]

dx = 1

# compute the value of the derivative of square() at x = 3 using each method
dydx1 = (square(3 + dx) - square(3)) / dx
dydx2 = (square(3) - square(3 - dx)) / dx
dydx3 = (square(3 + dx) - square(3 - dx)) / (2*dx)

# compute the y-intercept for each method
b1 = square(3) - dydx1*3
b2 = square(3) - dydx2*3
b3 = square(3 + dx) - dydx3*(3 + dx)

# compute the lines showing the different slopes (derivatives)
y1 = [a*dydx1 + b1 for a in x]
y2 = [a*dydx2 + b2 for a in x]
y3 = [a*dydx3 + b3 for a in x]

fig, ax = plt.subplots()

# plot lines
line0, = ax.plot(x, y0, label="y=(x-2)^2")
line1, = ax.plot(x, y1, label="forward")
line2, = ax.plot(x, y2, label="backward")
line3, = ax.plot(x, y3, ls="--", label="central")

# mark x - dx, x, and x + dx
ax.scatter([3 - dx, 3, 3 + dx], [square(3 - dx), square(3), square(3 + dx)], color="black", zorder=10)

# details
ax.grid()
plt.title("Comparison of Finite Difference Algorithms")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("finite_difference_algorithms.png", dpi=100)
plt.show()