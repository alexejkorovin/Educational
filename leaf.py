import sys
import stdarray
import stddraw
import stdrandom
import stdio
import fileinput



n = 1000
#with open('in.txt','r', encoding='utf-8') as f:
#    read_data = f.read()
#   print(read_data)

for line in fileinput.input('in.txt'):

    probabilities = stdarray.readFloat1D()
    cx = stdarray.readFloat2D()
    cy = stdarray.readFloat2D()





x = 0.0
y = 0.0
stddraw.setPenRadius(0.001)
for i in range(n):
    r = stdrandom.discrete(probabilities)
    x0 = cx[r][0] * x + cx[r][1] * y + cx[r][2]
    y0 = cy[r][0] * x + cy[r][1] * y + cy[r][2]
    x = x0
    y = y0
    stddraw.point(x, y)

stddraw.show()
