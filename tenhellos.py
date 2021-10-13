# -----------------------------------------------------------------------
# tenhellos.py
# -----------------------------------------------------------------------
import stdarray
import stdio
import sys
import random

m = int(sys.argv[1])
n = int(sys.argv[2])

a = stdarray.create2D(n+1, m+1, 0.0)
counter = 0
for i in range(m):
    for j in range(n):
        a[i][j] = counter
        counter += 1


for i in range(m):
# Average for row i
    total = 0.0
    for j in range(n):
        total += a[i][j]
    a[i][n] = total / m

for j in range(n):
 # Average for column j
 total = 0.0
 for i in range(m):
    total += a[i][j]
 a[m][j] = total / n


for i in range(m+1):
    for j in range(n+1):
        stdio.write(float(a[i][j]))
        if len(str(a[i][j])) < (len(max(a))):
            for k in range(len(max(a))):
                stdio.write(' ')

    stdio.writeln()

for i in range(m):
    stdio.write(a[n][i])
    if len(str(a[i][j])) < (len(max(a))):
        for k in range(len(max(a))):
            stdio.write(' ')


#for i in range(len(isPrime)):
 #   stdio.write(' isPrime'+'['+str(i)+']'+'='+str(isPrime[i]))

#for i in range(len(a)):
 #   stdio.write(' b'+'['+str(i)+']'+'='+str(a[i]))