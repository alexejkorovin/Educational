#-----------------------------------------------------------------------
# harmonic.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer n as a command-line argument. Write to standard
# output the value of the nth harmonic number.
if __name__ == '__main__':
    for idx, arg in enumerate(sys.argv):
       print("Argument #{} is {}".format(idx, arg))
    print ("No. of arguments passed is ", len(sys.argv))

for l in range(len(sys.argv)-1):
    n = int(sys.argv[l+1])

    total = 0.0
    for i in range(1, n+1):
        # Add the ith term to the sum
        total += 1.0 / i

    stdio.writeln(total)

#-----------------------------------------------------------------------

# python harmonic.py 2
# 1.5

# python harmonic.py 10
# 2.9289682539682538

# python harmonic.py 10000
# 9.787606036044348

