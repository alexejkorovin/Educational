import sys
import stdrandom
import stdio
from counter import Counter

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])

    heads = Counter('Heads', n)
    tails = Counter('Tails', n)

    for i in range(n):
        if stdrandom.bernoulli(p):
            heads.increment()
        else:
            tails.increment()
    heads.__count = -100
    stdio.writeln(heads)
    stdio.writeln(tails)


if __name__ == '__main__':
    main()