def binary(array, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary(array, low, mid - 1, x)
        else:
            return binary(array, mid + 1, high, x)
    else:
        return -1


def binary2(array, low, high, x):  # non recursive
    while high >= low:
        mid = (high + low) // 2
        if array[mid] > x:
            high = mid - 1
        elif array[mid] < x:
            low = mid + 1
        elif array[mid] == x:
            return mid
        else:
            return -1


def main():
    array = [1, 3, 4, 5, 6, 4, 55, 44, 32, 334, 234, 33, 66]
    text = ['hello', 'aaa', 'hello', 'one', 'new', 'world',]
    text.sort()
    array.sort()
    x = 44
    y = 'new'
    print(binary(text, 0, len(text) - 1, y))
    print(binary2(array, 0, len(array) - 1, x))


if __name__ == '__main__': main()
