def factorial(n):
    if n<0: return 0
    elif n == 1: return 1
    else:
        fact = 1
        while n>1:
            fact *=n
            n-=1
        return fact

def factorial2(n):
   if n ==1:
       return n
   else:
       return n*factorial2(n-1)

def main():

    print(factorial(1000000))

if __name__ == '__main__': main()
