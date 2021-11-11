import stddraw
import math
import sys
import plotfigure

stddraw.setXscale(0.0,25.0)
stddraw.setYscale(0.0, 25.0)
stddraw.setPenRadius(0.1)

a = float(sys.argv[1])
px = 1
py = 1
line = 1
for i in range(0, 120, 6):
    for j in range(0, 120, 6):
        plotfigure.drawsquareA(a, px+j, py+i)
        plotfigure.triangle(a, px+i, py + j)


stddraw.show()
