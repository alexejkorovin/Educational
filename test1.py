import sys
import stdio
import stdarray
from instream import InStream
""""
Compose a function isValidDNA() that takes a string as its argument and
returns True if and only if it consists entirely of the characters A, C, T, and G.
"""


def isValidDNA(dna):
    if len(dna) == 0: return True
    for i in range(len(dna)):
        print(dna)
        if dna[i] == "A" or dna[i] == "C" or dna[i] == "T" or dna[i] == "G":
            return isValidDNA(dna[1:len(dna)])
        else:
            return False


"""
takes a DNA string as its argument and returns its Watson–Crick complement: replace A with T, and C with G, and
vice versa
"""

def _readHTML(url1):
 page = InStream(url1)
 html = page.readAll()
 return html

def testDomain1(url1):
    html = str(url1)
    a = html.find("//", 0)
    b = html.find("/", a)
    return html[-3:b]



# def testDNA(s1, s2):
#     s1new = s1 + s1
#     s2new = s2 + s2
#     if len(s1)!=len(s2):
#         return False
#     if (s1 in s2new) and (s2 in s1new):
#         return True
#     else:
#         return False


def _main():
    """
    For testing:
    """
    import stdio
    # s1 = 'abcdda'
    # s2 = 'dabcda'
    url1 = "https://introcs.cs.princeton.edu/python/home/"
    print(testDomain1(url1))


if __name__ == '__main__':
    _main()
