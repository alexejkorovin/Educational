"""
Tile. Compose a program that takes
the name of an image file and two
integers m and n as command-line
arguments and creates an m-by-n
tiling of the picture.
"""

import stddraw
import sys
from picture import Picture


def scale_pic(source, wT, hT):
    stddraw.setXscale(-source.width(), source.width())
    stddraw.setYscale(-source.height(), source.height())
    target = Picture(wT, hT)
    for colT in range(wT):
        for rowT in range(hT):
            colS = colT * source.width() // wT
            rowS = rowT * source.height() // hT
            target.set(colT, rowT, source.get(colS, rowS))

    for i in range(-source.width(), source.width(), wT * 2):
        for j in range(-source.height(), source.height(), hT * 2):
            stddraw.picture(target, i + wT, j + hT)


def tile(filename, wT, hT):
    pic = Picture(filename)
    width = pic.width()
    height = pic.height()

    stddraw.setCanvasSize(width, height)
    scale_pic(pic, int(width / wT), int(height / hT))
    stddraw.show()


def main():
    filename = sys.argv[1]
    wT = int(sys.argv[2])
    hT = int(sys.argv[3])
    tile(filename, wT, hT)


if __name__ == '__main__': main()
