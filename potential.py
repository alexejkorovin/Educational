# -----------------------------------------------------------------------
# potential.py
# -----------------------------------------------------------------------
import sys
import gaussian
import stddraw
import stdarray
import random
from charge import Charge
from color import Color
from picture import Picture
from instream import InStream
from outstream import OutStream

MAX_GRAY_SCALE = 255

# Modify potential.py (Program 3.1.8) to take an integer n from the command
# line and generate n random Charge objects in the unit square, with potential
# values drawn randomly from a Gaussian distribution with mean 50 and standard
# deviation 10.
#
# sigma	=	standard deviation
# mu	=	mean

# Read charges from standard input into an array.
def rand_charges(n):

    ncharges = stdarray.create1D(3 * n, 0.0)

    for i in range(len(ncharges)):
        ncharges[i] = random.randrange(-50,50)

    for i in range(0,n * 3,3):
        x1 = ncharges[i]
        x2 = ncharges[i+1]
        ncharges[i] = float(gaussian.pdf(x1, mu=50.0, sigma=10.0))
        ncharges[i+1] = float(gaussian.pdf(x2, mu=50.0, sigma=10.0))
        ncharges[i + 2]=random.randrange(-100,100,10)
    return ncharges


def Potential(n, charges1):
    # instream = InStream(inFilenames)
    # charges1 = instream.readAllFloats()
    charges = stdarray.create1D(n)
    c = 0
    for i in range(0, n * 3, 3):
        x0 = charges1[i]
        y0 = charges1[i + 1]
        q0 = charges1[i + 2]
        charges[c] = Charge(x0, y0, q0)
        c += 1

    # Create a Picture depicting potential values.
    pic = Picture()
    for col in range(pic.width()):
        for row in range(pic.height()):
            # Compute pixel color.
            x = 1.0 * col / pic.width()
            y = 1.0 * row / pic.height()
            v = 0.0

            for i in range(n):
                v += charges[i].potentialAt(x, y)
            v = (MAX_GRAY_SCALE / 2.0) + (v / 2.0e10)
            if v < 0:
                grayScale = 0
            elif v > MAX_GRAY_SCALE:
                grayScale = MAX_GRAY_SCALE
            else:
                grayScale = int(v)
            color = Color(grayScale, grayScale, grayScale)
            pic.set(col, pic.height() - 1 - row, color)

    # Draw the Picture.
    stddraw.setCanvasSize(pic.width(), pic.height())
    stddraw.picture(pic)
    stddraw.show()


def _main():
    n = 9
    arr = rand_charges(n)
    inFilenames = 'charges.txt'
    Potential(n, arr)


if __name__ == '__main__':
    _main()

# -----------------------------------------------------------------------

# python potential.py < charges.txt
