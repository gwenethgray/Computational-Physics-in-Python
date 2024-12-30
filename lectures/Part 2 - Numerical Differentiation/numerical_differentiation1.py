# derivatives of functions or just arrays of data can be approximated by numerical methods

# finite difference method - forward difference
# @params:
#   func: a continuous function of one variable x
#   a: the value of x at which to compute the derivative
#   dx: the magnitude of finite difference over which the change in the function is calculated
def forward_fd(func, a, dx):
	dy = func(a + dx) - func(a)
	return dy / dx

from math import sin
import matplotlib.pyplot as plt

x = [i*0.01 for i in range(1000)]
y = [sin(a) for a in x]

dx = 1e-10 # very small amount


fig, ax = plt.subplots()
line0, = ax.plot(x, y, label="sin(x)")

for dx in [1.0, 0.5, 0.1, 0.05]:
	dydx = [forward_fd(sin, a, dx) for a in x]
	line, = ax.plot(x, dydx, label=f"dx = {dx}")

plt.legend()
plt.show()