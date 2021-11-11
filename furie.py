import sys
import matplotlib.pyplot as plt
import numpy as np

n = int(sys.argv[1])
# setting the x - coordinates
x = np.arange(0, 2 * (np.pi), 0.1)
# setting the corresponding y - coordinates

y = 0
for i in range(n):
    y += np.cos(i*x)
y = y/n
plt.plot(x, y)




# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
plt.show()