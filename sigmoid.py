import sys
import math

import stdio

a = float(sys.argv[1])


def stig(x):
    return 1 / (1 + math.exp(-x))


stdio.writeln(stig(a))
