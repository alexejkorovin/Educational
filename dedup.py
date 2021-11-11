import sys
import binarysearch

def dedup(a):
    a.sort()
    print(a)
    b = []
    b.append(a[0])
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            b.append(a[i])
    return b


def main():
    # text = str(sys.argv[1])
    text = "hello aaa hello one new world world"
    t = dedup(text.split())
    print(t)

if __name__ == '__main__': main()