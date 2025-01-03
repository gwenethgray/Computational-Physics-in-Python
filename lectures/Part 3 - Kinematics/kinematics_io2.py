import matplotlib.pyplot as plt

t, y = [], []

with open("freefall_data.csv", "r") as f:
	lines = f.readlines()
	header = lines[0]
	data = lines[1:]
	for line in data:
		t_i, y_i = line.split(",")
		t.append(float(t_i)) # convert from string to numeric!
		y.append(float(y_i))

plt.figure()
plt.plot(t, y)
plt.title("Free Fall due to Gravity")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.savefig("freefall.png", dpi=100)
plt.show()