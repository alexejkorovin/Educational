# Program to display the Fibonacci sequence up to n-th term
import stdarray
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
sequence = [0]*nterms
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        sequence[count] = n1
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

print(sequence)
newtyple = tuple(sequence)
print(newtyple)
num = int(input("which element to print? "))
print(newtyple[num])
first, *others, last = newtyple
