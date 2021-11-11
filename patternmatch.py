import stdio
import stopwatch
import matplotlib.pyplot as plt
import closenumbers
import random
import stdarray


def matching(array):
    row = len(array)
    col = len(array[0])
    subarray = [[0 for k in range(col)] for l in range(row)]

    for i in range(1,row):
        for j in range(1,col):
            if array[i][j] == 1:
                subarray[i][j] = min(subarray[i][j - 1], subarray[i - 1][j],
                              subarray[i - 1][j - 1]) + 1
            else:
                subarray[i][j] = 0
    max_of_s = subarray[0][0]
    max_i = 0
    max_j = 0
    for i in range(row):
        for j in range(col):
            if max_of_s < subarray[i][j]:
                max_of_s = subarray[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(array[i][j], end=" ")
        print("")




def main():
    array = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    matching(array)
    # print(matching(array))


if __name__ == '__main__': main()
