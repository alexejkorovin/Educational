import sys
import stdio

"""
translate from DNA to mRNA
(replace 'T' with 'U')
"""
def translate(dna):
    dna = dna.upper()
    rna = dna.replace('T', 'U')
    return rna




"""
extract file name
and extension from a
command-line argument
"""
def args():
    s = sys.argv[1]
    dot = s.find('.')
    base = s[:dot]
    extension = s[dot + 1:]







"""
is an arrayofstrings 
inascending
order?
"""
def isSorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


def main():
 """
 write all lines on standard
 input that contain a
 string specified as a
 command-line argument
 """

query = sys.argv[1]
while stdio.hasNextLine():
 s = stdio.readLine()
 if query in s:
     stdio.writeln(s)


 if __name__ == '__main__':
  main()