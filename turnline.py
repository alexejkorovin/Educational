import stddraw
import math
import sys
import numpy as np
from scipy.ndimage import rotate

from typing import Any, Tuple

# stddraw.setXscale(-4.0, 4.0)
# stddraw.setYscale(-4.0, 4.0)


def turn(angle,x0,y0,x1,y1):


    m1 = [[x0, y0], [x1, y1]]
    # stddraw.line(x0,y0,x1,y1)
    #stddraw.line(m1[0][0], m1[0][1])
    # for i in range(360):
    angle_degrees = np.radians(angle)
    x0 = np.cos(angle_degrees)*x0-np.sin(angle_degrees)*y0
    x1 = np.cos(angle_degrees)*x1-np.sin(angle_degrees)*y1
    y0 = np.sin(angle_degrees)*x0+np.cos(angle_degrees)*y0
    y1 = np.sin(angle_degrees)*x1+np.cos(angle_degrees)*y1
    stddraw.line(x0, y0, x1, y1)









def main():

    stddraw.setPenRadius(0.0)
    turn()
    stddraw.show()


if __name__ == '__main__':
    main()
