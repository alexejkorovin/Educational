import stddraw
import math
import sys
import  stdarray
import random

stddraw.setXscale(0, 100)
stddraw.setYscale(0, 100)

number = int(sys.argv[1])
p = float(sys.argv[2])
minrad = int(sys.argv[3])
maxrad = int(sys.argv[4])

a = stdarray.create1D(number, 0.0)
b = stdarray.create1D(number, 0.0)

for i in range(number):
    x = random.randrange(0, 100, 1)
    y = random.randrange(0, 100, 1)
    a[i] = x
    b[i] = y




for i in range(number):
    for j in range(number):
        possibility = random.random()
        if possibility <= p:
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledCircle(a[i], b[j], random.randrange(minrad, maxrad, 1))
        else:
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.filledCircle(a[i], b[j], random.randrange(minrad, maxrad, 1))
stddraw.show()