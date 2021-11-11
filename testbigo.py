import time
from random import randint


import numpy as np

import factorial1
import stdarray
import matplotlib.pyplot as plt

list1 = np.array([i for i in range(1,31)])


times=[]


for i in range(30):

    start_time = time.time()
    list2 = factorial1.factorial2(list1[i])
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
print(times)



# x = [2, 4, 6, 8, 10, 12]
#
# time = [4, 8, 12, 16, 20, 24]

plt.xlabel("No. of elements")
plt.ylabel("Time required")
plt.plot(list1, times)
#plt.draw()
plt.show()