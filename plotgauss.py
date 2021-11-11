import sys
import stdarray
import gaussian
import stdstats
import stddraw

n = int(sys.argv[1])
a = stdarray.create1D(n+1, 0.0)
for i in range(n+1):
    a[i] = gaussian.pdf(-4.0 + 8.0 * i / n)
stdstats.plotPoints(a)
stdstats.plotLines(a)
stddraw.show()

