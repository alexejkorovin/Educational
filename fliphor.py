import sys
import stddraw
from color import Color
from picture import Picture

pic = Picture(sys.argv[1])
picnew = Picture(pic.width(), pic.height())
t = int(pic.height())
for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col, row)
        picnew.set(t-col, row, pixel)

stddraw.setCanvasSize(picnew.width(), picnew.height())
stddraw.picture(picnew)
stddraw.show()

