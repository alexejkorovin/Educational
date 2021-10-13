import stddraw
import math
import sys
import stdarray
import random

stddraw.setXscale(0, 12)
stddraw.setYscale(0, 12)

dots = int(sys.argv[1])
radius = int(sys.argv[2])
p = float(sys.argv[3])

a = stdarray.create1D(dots, 0.0)
b = stdarray.create1D(dots, 0.0)


def circle(i, radius):
    r = 4 + (+-math.sqrt(radius^2-i*i))
    return r


for i in range(0, dots):

        y = circle(i, radius)

        a[i] = i
        b[i] = y
        x = a[i]
        stddraw.point(x, y)



for i in range(dots):
    for j in range(dots):
        possibility = random.random()
        if possibility <= p:
            stddraw.line(a[i], b[i], a[j], b[j])
stddraw.show()
