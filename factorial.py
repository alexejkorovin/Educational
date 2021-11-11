import math
import sys
import stdio


def fact(a):
    if a == 0: return 1
    return a * fact(a - 1)



def main():
    a = int(sys.argv[1])
    print(fact(a))


if __name__ == '__main__': main()
