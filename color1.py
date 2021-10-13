import sys
import stddraw
from color import Color
from picture import Picture
r1 = int(sys.argv[1])
g1 = int(sys.argv[2])
b1 = int(sys.argv[3])
c1 = Color(r1, g1, b1)

stddraw.setPenColor(c1)

stddraw.setPenColor(c1)

pic = Picture(256, 256)
for col in range(256):
    for row in range(256):
        pic.set(col, row,c1)

stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()

