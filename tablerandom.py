# -----------------------------------------------------------------------
# bouncingball.py
# -----------------------------------------------------------------------
import sys
import math
import stddraw
import random

# Draw a bouncing ball to standard draw.


DT = 100.0
n = int(sys.argv[1])
scaleX = 100.0
scaleY = 1000.0
stddraw.setXscale(0.0, scaleX)
stddraw.setYscale(0.0, scaleY)

a = 0
b = 0
c = 0
shift = 0.0
for i in range(n):
    # Update ball position and draw it there.
    if shift > scaleX/3:
        stddraw.setXscale(0.0, scaleX+shift)
        scaleX = shiftg
    if (a and b and c) > scaleY:
        t = max(a, b, c)
        stddraw.setYscale(0.0, scaleY+t)
        scaleY = t
    a += random.randrange(0, 20, 1)
    b += random.randrange(0, 20, 1)
    c += random.randrange(0, 20, 1)
    stddraw.filledRectangle((5+shift), 5, 5, a)
    stddraw.filledRectangle((15+shift), 5, 5, b)
    stddraw.filledRectangle((25+shift), 5, 5, c)
    shift += 1

    stddraw.show(DT)
    stddraw.clear(stddraw.GRAY)
# -----------------------------------------------------------------------

# python bouncingball.py

