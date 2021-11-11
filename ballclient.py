import sys
import random
import stdarray
import stddraw
from instream import InStream
from outstream import OutStream
from ballb import OneBall
from ballb import Ball

def randPos(n):
    outstream = OutStream('outpos.txt')
    arr1 = stdarray.create1D(n * 4, "")
    for i in range(n * 4):
        arr1[i] = round(random.random(), 3)
    outstream.write(str(n)+'\n')
    for i in range(n * 4):
        outstream.write(str(arr1[i])+' ')




stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
numberofballs = int(sys.argv[1])
randPos(numberofballs)
newballs = Ball('outpos.txt')
RADIUS = .05
DT = 20.0
while True:
    stddraw.clear()
    newballs.draw()
    stddraw.show(10)
    stddraw.show(DT)