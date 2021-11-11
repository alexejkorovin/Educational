import sys
import stddraw
from color import Color
from picture import Picture
import numpy as np
import matplotlib.pyplot as plt

pic = Picture(sys.argv[1])
picr = Picture(pic.width(), pic.height())
picg = Picture(pic.width(), pic.height())
picb = Picture(pic.width(), pic.height())

for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col, row)
        r = pixel.getRed()
        g = pixel.getGreen()
        b = pixel.getBlue()
        RED = Color(r, 0, 0)
        GREEN = Color(0, g, 0)
        BLUE = Color(0, 0, b)

        picr.set(col, row, RED)
        picg.set(col, row, GREEN)
        picb.set(col, row, BLUE)


stddraw.setCanvasSize(pic.width()*2, pic.height()*2)
stddraw.picture(picb)

stddraw.show()

