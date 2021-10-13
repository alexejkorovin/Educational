import stddraw
import math
import sys

def triangle(a, px, py):
    stddraw.line(px,py,px+a,py)
    h = math.sqrt(a * a - (a * a)/4)
    stddraw.line(px, py, px + a/2, py + h)
    stddraw.line(px+a, py, px + a/2, py + h)

def drawsquareA(a, px, py):
    stddraw.line(px, py, px+a,py)
    stddraw.line(px+a, py, px+a,py+a)
    stddraw.line(px+a,py+a, px, py+a)
    stddraw.line(px,py+a, px, py)

def main():
    stddraw.setXscale(0.0, 25.0)
    stddraw.setYscale(0.0, 25.0)
    stddraw.setPenRadius(0.1)
    a = float(sys.argv[1])
    px = float(sys.argv[2])
    py = float(sys.argv[3])
    drawsquareA(a, px, py)
    triangle(a, px, py)
    stddraw.show()
if __name__ == '__main__': main()
