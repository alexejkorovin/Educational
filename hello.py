#-----------------------------------------------------------------------
# quadratic.py
#-----------------------------------------------------------------------

import stdio
import sys
import math
#Initialize the largest and smallest values as 'None'
largest  = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == "finish": #Type 'finish' to get the output
        break
    try:
        fnum = float(num)  #Convert input to float

        #Get largest value
        if largest is None:
            largest = fnum
        elif fnum > largest:
            largest = fnum

        #Get smallest value
        elif smallest is None:
            smallest = fnum
        elif fnum < smallest:
            smallest = fnum

    except:
        #If the user input is not 'finish' or a number
        print("Invalid input")
        continue


print("Largest value is",largest)
print("Smallest value is",smallest)