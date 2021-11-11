import sys
import stdio



# positive_int_generator1 = lambda n: big_o.datagen.large_integers(10000)


def gcd(p, q):
    if q == 0: return p
    return gcd(q, p % q)

def gcd2(x, y):
    while (y):
        x, y = y, x % y
    return x


def main():
    p = int(sys.argv[1])
    q = int(sys.argv[2])

    stdio.writeln(gcd2(p, q))



if __name__ == '__main__': main()

# best, others = big_o.big_o(gcd, positive_int_generator1, n_repeats=100)
# print(best)
