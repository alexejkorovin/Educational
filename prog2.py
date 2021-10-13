

# def _readHTML(url1):
#     page = InStream(url1)
#     html = page.readAll()
#     return html


def reverseDomain1(url1):
    arr = url1.split('/')

    return arr[::-1]


def mystery(s):
    n = len(s)
    if (n <= 1): return s
    a = s[0: n // 2]
    b = s[n // 2: n]
    return mystery(b) + mystery(a)




def _main():
    t1 = "12345678"
    t = 'https://stackoverflow.com/questions/'
    print(mystery(t1))


if __name__ == '__main__':
    _main()
