import sys
import stdio
import stdarray
import math
total = 0


def majority(a, b, c):
    return a and b or a and c or b and a or b and c or c and b or c*a

while not stdio.isEmpty():
    a = stdio.readBool()
    b = stdio.readBool()
    c = stdio.readBool()
    stdio.writeln(majority(a, b, c))