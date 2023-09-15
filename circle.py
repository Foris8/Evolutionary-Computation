iimport matplotlib.pyplot as plt
import random
import math

# Set random seed for reproducibility
np.random.seed(0)

# radius of the circle
circle_r = 1

# center of the circle (x, y)
circle_x = 0
circle_y = 0
x = []
y = []

# random radius
r = circle_r * math.sqrt(random.random())

# calculating coordinates
for i in range(0,100):
	alpha = 2 * math.pi * random.random()
	x.append(r * math.cos(alpha) + circle_x)
	y.append(r * math.sin(alpha) + circle_y)

plt.ylim(-2, 2)
plt.xlim(-2, 2)
plt.scatter(x, y, cmap='viridis')
plt.title('Points in a circle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
