import sys
import random
import stdarray
import stddraw
from instream import InStream
from outstream import OutStream
from body import Body
from instream import InStream
from vector import Vector


# -----------------------------------------------------------------------
class OneBall:
    def __init__(self, rx, ry, vx, vy):
        self._rx = rx
        self._ry = ry
        self._vx = vx
        self._vy = vy

    def draw(self, RADIUS=.05):
        stddraw.clear(stddraw.GRAY)
        stddraw.filledCircle(self._rx, self._ry, RADIUS)

    def move(self, RADIUS=.05):

        if abs(self._rx + self._vx) + RADIUS > 1.0:
            self._vx = -self._vx
        if abs(self._ry + self._vy) + RADIUS > 1.0:
            self._vy = -self._vy
        self._rx = self._rx + self._vx
        self._ry = self._ry + self._vy

class Ball:
    def __init__(self, filename):
        instream = InStream(filename)
        stddraw.setXscale(-1.0, 1.0)
        stddraw.setYscale(-1.0, 1.0)
        n = instream.readInt()

        self._bodies = stdarray.create1D(n * 4)
        for i in range(n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            self._bodies[i] = OneBall(rx, ry, vx, vy)

    def draw(self):
        for t in self._bodies:
            t.draw()


# -----------------------------------------------------------------------

def main():
    stddraw.setXscale(-1.0, 1.0)
    stddraw.setYscale(-1.0, 1.0)
    numberofballs = int(sys.argv[1])
    newballs = Ball('outpos.txt')
    RADIUS = .05
    DT = 20.0
    while True:
        stddraw.clear()
        newballs.draw()
        stddraw.show(10)
        stddraw.show(DT)
if __name__ == '__main__':
        main()
