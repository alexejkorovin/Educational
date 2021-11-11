import stdarray
import stdstats
import stddraw


def tone(hz, t):
    stddraw.setYscale(-6.0, 6.0)
    hi = tone(440, 0.01)
    stdstats.plotPoints(hi)
    stddraw.show()

def plotPoints(a):
    n = len(a)
    stddraw.setXscale(0, n-1)
    stddraw.setPenRadius(1.0 / (3.0 * n))
    for i in range(n):
        stddraw.point(i, a[i])

def plotLines(a):
    n = len(a)
    stddraw.setXscale(0, n-1)
    stddraw.setPenRadius(0.0)
    for i in range(1, n):
        stddraw.line(i-1, a[i-1], i, a[i])

def plotBars(a):
    n = len(a)
    stddraw.setXscale(0, n-1)
    for i in range(n):
        stddraw.filledRectangle(i-0.25, 0.0, 0.5, a[i])

n = 20
a = stdarray.create1D(n, 0.0)
for i in range(n):
    a[i] = 1.0 / (i + 1)
plotBars(a)
stddraw.show()