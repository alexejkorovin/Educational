import stddraw
import math
import sys

stddraw.setXscale(0, 100)
stddraw.setYscale(0, 100)
stddraw.setPenRadius(0.5)
stddraw.setPenColor(stddraw.BLACK)


def draw_bar(x, t):
    if t:
        stddraw.line(x, 5, x, 40)
    if t == 0:
        stddraw.line(x, 5, x, 20)
    return


def draw_number(number, position):
    if number == 0:
        draw_bar(position, True)
        draw_bar(position + 2, True)
        draw_bar(position + 4, False)
        draw_bar(position + 6, False)
        draw_bar(position + 8, False)
    if number == 1:
        draw_bar(position, False)
        draw_bar(position + 2, False)
        draw_bar(position + 4, False)
        draw_bar(position + 6, True)
        draw_bar(position + 8, True)
    if number == 2:
        draw_bar(position, False)
        draw_bar(position + 2, False)
        draw_bar(position + 4, True)
        draw_bar(position + 6, False)
        draw_bar(position + 8, True)
    return


position = 4
stddraw.line(2, 5, 2, 40)
for i in range(0, 3):
    draw_number(i, position)
    position += 11
stddraw.show()
