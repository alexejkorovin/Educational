# -----------------------------------------------------------------------
# spiral.py
# -----------------------------------------------------------------------

import math
import sys
import stddraw
from turtle import Turtle

# -----------------------------------------------------------------------
stddraw.setXscale(-10.0, 10.0)
stddraw.setYscale(-10.0, 10.0)
stddraw.setCanvasSize(860,860)
n = int(sys.argv[1])

angle = 180-360/n/2
step = 8
turtle = Turtle(1, 0, angle)

stddraw.setPenRadius(0.0)
stddraw.clear(stddraw.LIGHT_GRAY)

for i in range(n*2):
    turtle.goForward(step)
    turtle.turnLeft(angle)

stddraw.show()


# -----------------------------------------------------------------------

