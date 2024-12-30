# we can access code in other files (modules) by importing them
import vector
# and we can import specific classes or functions from a library
# from vector import Vector

# classes defined in the module can be accessed by dot notation as if they were attributes of an object representing the module
posn = vector.Vector(1, 2)
mag = posn.magnitude()

# there are useful libraries full of modules for computational physics, like "math" the python standard library
import math

x_vals = list(range(10))
y_exp = [math.exp(x) for x in x_vals]
y_sin = [math.sin(x) for x in x_vals]
y_cos = [math.cos(x) for x in x_vals]
y_tan = [math.tan(x) for x in x_vals]

# matplotlib is standard for visualization
import matplotlib.pyplot as plt

# make a figure
# plt.figure()
# plt.plot(x_vals, y_exp)
# plt.show()

# math has many optimized functions which are much faster for certain common problems than using several python operators
posns = [vector.Vector(i, i) for i in range(10)]
mags = [math.hypot(p.x, p.y) for p in posns]

# it is very important to consider computational complexity for physics applications, because un-optimized code can take too much time to run
import time

N_posns = [10**i for i in range(2,8)]
T_with_power_operators = []
T_with_hypot = []

for N in N_posns:
	posns = [vector.Vector(10,10) for i in range(N)]
	time_start = time.time()
	mags_with_power_operators = [p.magnitude() for p in posns]
	time_stop = time.time()
	T_with_power_operators.append(time_stop - time_start)

	time_start = time.time()
	mags_with_hypot = [math.hypot(p.x, p.y) for p in posns]
	time_stop = time.time()
	T_with_hypot.append(time_stop - time_start)


plt.figure()
plt.title("Time Complexity of Vector Magnitude Computations")
plt.xlabel("Number of Vectors")
plt.ylabel("Time (s)")
plt.plot(N_posns, T_with_power_operators, label="** Operators")
plt.plot(N_posns, T_with_hypot, label="Math.hypot()")
plt.legend()
plt.savefig("algorithmic_complexity.png", dpi=100)
plt.show()