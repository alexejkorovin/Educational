import sys
import stdio
import numpy
import numpy as np
import matplotlib.pyplot as plt

class Square:
    def __init__(self,n):
        self._value = n

    def sq(self):
        return self._value * self._value

    def line(self):
        return self._value *4+5

def bisect(f, y, lo1, hi1, delta=0.0000001):

    mid = (hi1 + lo1) / 2.0
    f = Square(mid)
    if (hi1 - lo1) < delta:
        return mid
    if f.line() > y:
        return bisect(f, y, lo1, mid, delta)
    else:  # if f(mid)<y:
        return bisect(f, y, mid, hi1, delta)


def square(data):
    list = data
    for i in range(len(data)):
        list[i] = data[i] * data[i]
    return list

def linef(data):
    list = data
    for i in range(len(data)):
        list[i] = data[i] *4+5
    return list


def main():

    y = 25

    data_1 = []  # empty regular list
    for i in range(0, 200):
        arr = i
        data_1.append(arr)
    data = np.array(data_1)  # transformed to a numpy array
    f = linef(data)
    sorted_data = numpy.sort(f)

    print("The CDF result is-", f)
    fig = plt.figure()
    fig.suptitle('CDF of data points')
    ax2 = fig.add_subplot(111)
    ax2.plot(data_1, f)
    ax2.set_xlabel('sorted_random_data')
    ax2.set_ylabel('f')
    x = bisect(f, y, 0, 200)
    stdio.writef('%.3f\n', x)
    plt.show()


if __name__ == '__main__': main()
