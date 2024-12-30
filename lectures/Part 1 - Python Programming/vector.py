# a class is a pattern for defining objects with attributes which can be accessed by dot notation
class Vector:
	# constructor
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# classes can also have other method functions
	def magnitude(self):
		return (self.x**2 + self.y**2)**0.5

	# compute unit normal vector
	def norm(self):
		mag = self.magnitude()
		return Vector(self.x/mag, self.y/mag)

	# dot product with another vector
	def dot(self, vec):
		return self.x * vec.x + self.y * vec.y

	# you can overload built-in methods, including operators!
	# now you can add Vector(1,2) + Vector(2,3) and get another vector
	def __add__(self, vec):
		return Vector(self.x + vec.x, self.y + vec.y)

	# vector subtraction: Vector(1,2) - Vector(2,3)
	def __sub__(self, vec):
		return Vector(self.x - vec.x, self.y - vec.y)

	# what shows up when a Vector instance is converted to a string, such as in the print() function
	def __repr__(self):
		return f"Vector({self.x},{self.y})"