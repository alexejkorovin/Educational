import stdarray 
import stdio
import sys

n = int(sys.argv[1])
linkCounts = stdarray.create2D(n, n, 0) 
outDegrees = stdarray.create1D(n, 0)

while not stdio.isEmpty():
# Accumulate link counts.
    i = stdio.readInt()
    j = stdio.readInt()
    outDegrees[i] += 1
    linkCounts[i][j] += 1

stdio.writeln(str(n) + ' ' + str(n))
for i in range(n): 
    # Write probability distribution for row i.
    for j in range(n):
        # Write probability for column j.
        p = (0.90 * linkCounts[i][j] / outDegrees[i]) + (0.10 / n)
        stdio.writef('%8.5f', p)
    stdio.writeln()