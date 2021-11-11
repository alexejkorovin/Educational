import sys
import stdio
import stdarray

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


def complementWC(dna):
    newdna = ""
    for i in range(len(dna)):
        if dna[i] == 'T':
            newdna += 'A'
            continue
        if dna[i] == 'G':
            newdna += 'C'
            continue
        if dna[i] == 'A':
            newdna += 'T'
            continue
        if dna[i] == 'C':
            newdna += 'G'
            continue

    return newdna


def _main():
    """
    For testing:
    """
    import stdio

    dna = "AAACCCGGTTT"
    stdio.writeln(dna)
    print(complementWC(dna))


if __name__ == '__main__':
    _main()
