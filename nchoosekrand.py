
import stdarray


def comb(data,arr, new_str, k):
    if len(new_str) == k:
        print(new_str)
        return
    else:
        for i in range(len(arr)):
            if data[i] != True:
                new_str += arr[i]
                data[i] = True
                comb(data, arr, new_str, k)
                new_str = new_str[:-1]
                data[i] = False

def main():
    arr = ['a', 'b', 'c', 'd']
    data = [False, False, False, False]
    k = 3
    comb(data, arr, "", k)

if __name__ == '__main__': main()