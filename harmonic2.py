
import stdio
import sys

def harmoic(n):
    total = 0.0
    for i in range(1, n+1):
        # Add the ith term to the sum
        total += 1.0 / i
    stdio.writeln(total)
    return total


for l in range(1, len(sys.argv)):
    n = int(sys.argv[l])
    harmoic(n)

