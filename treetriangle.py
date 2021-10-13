import stddraw
import math
import sys
import numpy as np
from scipy.ndimage import rotate

from typing import Any, Tuple

DT = 20





def triangle(n, a, x, y):
    if n == 0:
        return

    h = math.sqrt(a * a - (a * a) / 4)

    x0 = x - a / 2
    x1 = x + a / 2
    y0 = y - a / 2
    y1 = y + h / 2

    m1 = [[x, y1], [x0, y0], [x0, y0], [x1, y0], [x1, y0], [x, y1]]



    stddraw.line(m1[0][0], m1[0][1], m1[1][0], m1[1][1])
    stddraw.line(m1[2][0], m1[2][1], m1[3][0], m1[3][1])
    stddraw.line(m1[4][0], m1[4][1], m1[5][0], m1[5][1])

    m1 = rotate(m1, angle=45, reshape=False)



    triangle(n - 1, a / 2, x0, y0)
    triangle(n - 1, a / 2, x1, y0)
    triangle(n - 1, a / 2, x, y1)

    stddraw.show(DT)


def main():
    n = int(sys.argv[1])
    stddraw.setPenRadius(0.0)
    triangle(n, .5, .5, .5)
    stddraw.show()


if __name__ == '__main__':
    main()
