import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    a = random.random()
    b = random.random()
    x = np.linspace(-10,10,1000)
    y = a*x+b
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()