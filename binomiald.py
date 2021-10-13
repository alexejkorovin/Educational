import math
import sys
import stddraw
import stdarray
import stdio

def draw(a, which):
    n = len(a)
    stddraw.setXscale(-1, n)
    stddraw.setYscale(-1, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n - i - 1, 0.5)

def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def binomial(n, k):
    if k == n:
        return '1'
    elif k == 1:
        return str(n)
    elif k > n:
        return '0'
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        c = math.factorial(n - k)
        return a // (b * c)


def pascal(n):
    triangle = stdarray.create2D(n,n, 0)
    for n in range(n ):
        triangle[n] = [1]
        for k in range(1, n + 1):
            triangle[n].append(int(binomial(n, k)))
    return triangle

def main():
    n = int(sys.argv[1])
    stdio.writeln(pascal(n))


if __name__ == '__main__': main()