import stddraw
import math
import sys

from scipy.ndimage import rotate

stddraw.setXscale(0.0, 1.0)
stddraw.setYscale(0.0, 1.0)

DT = 20


def vertical(n, x0, y0, x1, y1):
    if n == 0: return
    stddraw.line(x0/2, y0, x1/2, y1)
    return vertical(n - 1, x0/2, y0, x1/2, y1)
    stddraw.show(DT)


def horizotal(n, x0, y0, x1, y1):
    if n == 0: return
    stddraw.line(x0, y0 / 2, x1, y1 / 2)
    return horizotal(n-1, x0, y0 / 2, x1, y1 / 2)
    stddraw.show(DT)


def main():
    n = int(sys.argv[1])
    stddraw.setPenRadius(0.0)
    x0 = 0
    x1 = 1
    y0 = 1
    y1 = 1
    horizotal(n, x0, y0, x1, y1)
    vertical(n, 1, 0, x1, y1)
    stddraw.show()


if __name__ == '__main__':
    main()
