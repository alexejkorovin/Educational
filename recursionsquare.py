import stddraw
import sys
import color

DT = 200

stddraw.setXscale(0.0, 1.0)
stddraw.setYscale(0.0, 1.0)


def square(n, x, y, r):

    if n == 0:
        return



    stddraw.square(x + r, y + r, r / 2)
    stddraw.square(x - r, y + r, r / 2)
    stddraw.square(x + r, y - r, r / 2)
    stddraw.square(x - r, y - r, r / 2)

    square(n - 1, x + r, y + r, r / 2)
    square(n - 1, x - r, y + r, r / 2)
    square(n - 1, x + r, y - r, r / 2)
    square(n - 1, x - r, y - r, r / 2)
    stddraw.show(DT)

    stddraw.setPenColor(color.GRAY)
    stddraw.filledSquare(x, y, r)
    stddraw.setPenColor(color.BLACK)
    stddraw.square(x, y, r)





def main():
    n = int(sys.argv[1])
    square(n, 0.5, 0.5, .1)

    stddraw.show()


if __name__ == '__main__':
    main()
