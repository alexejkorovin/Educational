import math
import sys



def fact(a):
    if a == 0: return 1
    return a * fact(a - 1)

def sumlist(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0]+sumlist(list[1:])

def fibonacci(n):
    arr = (n+1)*[0]
    arr[0] = 0
    arr[1] = 1
    for i in range(1, n):
        arr[i + 1] = arr[i] + arr[i - 1]
    return arr[:-1]

#the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)

def sumn(n):
    if n < 1: return 0
    else:
        return n+sumn(n-2)
def harmonic(n):
    if n < 2: return 1
    return 1/n+(harmonic(n-1))

def recursionpow(k,n):
    if n == 0: return 1
    if n == 1: return k
    if k == 0: return 0
    return k*recursionpow(k, n-1)

def maxnumber(list):
    if len(list) == 1: return list[0]
    else:
        m = maxnumber(list[1:])
        return m if m > list[0] else list[0]

def main():

    #a = int(sys.argv[1])
    #print(fact(a))
    list = [1,22,11,8,5]
    #print(fibonacci(10))
    print(maxnumber(list))

if __name__ == '__main__': main()
