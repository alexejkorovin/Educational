import stdarray
import stdio


def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    for j in range(n):
        isFull[0][j] = isOpen[0][j]
    for i in range(1, n):
        for j in range(n):
            if isOpen[i][j] and isFull[i-1][j]:
                isFull[i][j] = True
    return isFull

def percolates(isOpen):
    isFull = flow(isOpen)
    n = len(isFull)
    for j in range(n):
        if isFull[n - 1][j]: return True
    return False


def main():
    isOpen = [[1, 0, 1], [0, 0, 0], [1, 1, 0]]
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))


if __name__ == '__main__': main()
