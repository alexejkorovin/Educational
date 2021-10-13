import sys
import stdio

#1011
def binary(a):
    if a == 0: return 0
    return a % 2 + 10*binary(a // 2)



def main():
    a = int(sys.argv[1])
    print(binary(a))


if __name__ == '__main__': main()
