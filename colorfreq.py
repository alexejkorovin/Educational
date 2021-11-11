import sys
import stddraw
import stdarray
from color import Color
from picture import Picture
import matplotlib.pyplot as plt
import numpy as np

def luminance(c):
    red = c.getRed()
    green = c.getGreen()
    blue = c.getBlue()
    return .299 * red + .587 * green + .114 * blue


def toGray(c):
    y = int(round(luminance(c)))
    return Color(y, y, y)


pic = Picture(sys.argv[1])

for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col, row)
        gray = toGray(pixel)
        pic.set(col, row, gray)

colorFreq = stdarray.create1D(256,0)
for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col, row)
        t = int(pixel.getRed())
        colorFreq[t] += 1


x = np.arange(0, 256 , 1)
# setting the corresponding y - coordinates


plt.plot(x, colorFreq)


plt.title("Color Frequency")
plt.show()


# stddraw.setCanvasSize(pic.width(), pic.height())
# stddraw.picture(pic)
# stddraw.show()
