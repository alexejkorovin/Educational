import stddraw
import math
stddraw.setXscale(0.5, 7.5)
stddraw.setYscale(0.5, 7.5)

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledSquare(i, j, 0.5)
        elif i % 2 != 0 and j % 2 != 0:
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledSquare(i, j, 0.5)
        elif i % 2 == 0 and j % 2 != 0:
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.square(i, j, 0.5)
        elif i % 2 != 0 and j % 2 == 0:
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.square(i, j, 0.5)

stddraw.show()