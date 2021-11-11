"""
Closest pair. Design a quadratic algorithm
 that finds the pair of integers
that are closest to each other.
(In the next section you will be asked to find a linearithmic algorithm.)
"""
import stdarray

def numbers_2(array):
    array.sort()
    result = stdarray.create1D(len(array)-1, '')
    for i in range(len(array)-1):
        result[i] = str(array[i]) + ':' + str(array[i+1])
    return result

def numbers(array):
    m = max(array)
    sorted = array[:]
    sorted.sort()
    result = stdarray.create1D(len(sorted) - 1, '')
    for i in range(len(sorted) - 1):
        d=m
        for j in range(i + 1, len(sorted)):
            d1 = abs(sorted[i] - sorted[j])
            if d1 <= d:
                d = d1
                result[i] = str(sorted[i]) + ':' + str(sorted[j])
    return result


def main():
    array = [1, 6,4, 6, 8, 14,8,8 , 0.1, 3, 2]
    print(numbers(array))
    print(numbers_2(array))


if __name__ == '__main__': main()
