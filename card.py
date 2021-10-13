import stdio
import stdarray
import sys


a = stdarray.create1D(10, 0)

for i in range(10):
    a[i] = stdio.readInt()

def check(a):
    t = 2*a
    if t//10 == 0:
        return t
    else:
        t1 = t//10
        t2 = (t % 10)
        t = t1+t2
        return t
values = 0
for i in range(10):
    if i%2 == 0:
        values += a[i]
        stdio.writeln(values)
    if i%2 != 0:
        values += check(a[i])
        stdio.writeln(values)

stdio.writeln(values)
if values % 10 ==0:
    stdio.writeln('valid')

