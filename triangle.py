import stddraw
import stdrandom
import sys

stddraw.setXscale(0.0, 1.0)
stddraw.setYscale(0.0, 1.0)

n = int(sys.argv[1])

DT = 2.0

cx = [0.000, 1.000, 0.500]
cy = [0.000, 0.000, 0.866]
x = 0.0
y = 0.0
count = 0
for i in range(10000):

 if count > 1000:
  stddraw.clear(stddraw.GRAY)
  stddraw.setXscale(0.0, 0.1)
  stddraw.setYscale(0.0, 0.1)

 r = stdrandom.uniformInt(0, 3)
 x = (x + cx[r]) / 2.0
 y = (y + cy[r]) / 2.0
 count += count
 stddraw.point(x, y)
 stddraw.show(DT)