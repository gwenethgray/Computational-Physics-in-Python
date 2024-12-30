# variables can hold numeric data to represent position
# = is the assignment operator, assigns the evaluated right hand side to the name on the left hand side
x = 2 # an integer (int)
y = 4.0 # a floating point number (float)

# the type() function can be used to check the type of a value (if passed a variable name, it evaluates the variable)
# the "assert" keyword raises an error if the following expression evaluates to False, and does nothing if it evaluates to True
assert type(x) == int
assert type(y) == float

# arithmetic operators
x1 = x + 1
y1 = y + 3
# x1 = x0 - 1
# x1 = x0 * 3
# x1 = x0 ** 5 --> power operator
# x1 = x0 / 2
# x1 = x0 % 4
# in-place arithmetic operators combine the assignment operator with others
# x1 += 1
# x1 -= 2
# x1 *= 5
# x1 /= 3

# sequences are objects that can hold multiple spatial coordinates in one variable
posn = (x, y) # a tuple, which is immutable - can't change values
posn_x = posn[0] # but tuples are ordered, so you can select elements in them by index operator []
posn_y = posn[1]

# a function to move the x coordinate of a position
def move_x(posn: tuple, dx: float):
	# adding a float to an int will turn the int into a float
	# adding an int to a float will keep the float a float
	return (posn[0] + dx, posn[1])

# a function to move both coordinates of a position
def move_xy(posn: tuple, dx: float, dy: float):
	return (posn[0] + dx, posn[1] + dy)

# a list is a mutable sequence
posn = [1, 2] # re-assigns a new value to the already defined variable named posn
posn[0] = 3 # re-assigns a new value to the first element in the list

# a list can also hold other sequences as elements
posns = [(0,0), (1,1), (2,2), (3,3)]

# a dictionary (dict) is a collection of key-and-value pairs, and can be indexed by the key value
posns = {"x": [0, 1, 2, 3], "y": [0, 1, 2, 3]}
posns_x = posns["x"]
assert type(posns_x) == list

# the range(start, stop) function creates a sequence of values from start to stop
# it is another type of sequence called a "range", but can be converted to a list
x = range(10)
x = list(x)
y = list(range(10))

# for-loops can iterate over elements in an "iterable" (ordered) sequence like a tuple, list, or range
for i in range(10):
	assert i == x[i]

# list comprehensions can define in-place new lists relative to other iterables
z = [i*2 for i in range(10)]

print(z)