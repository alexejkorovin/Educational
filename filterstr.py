import stdio
import sys
import stdarray
from instream import InStream
from outstream import OutStream

"""
    Compose a filter that reads text
    from an input stream and writes 
    it to an output stream, removing
    any lines that consist only of 
    whitespace
"""



def filter(inFilenames, outFilename, symbol1, symbol2):
    instream = InStream(inFilenames)
    outstream = OutStream(outFilename)
    s = instream.readAll()
    s = s.replace(symbol1, symbol2)
    outstream.write(s)

def _main():
    inFilenames = sys.argv[1]
    outFilename = sys.argv[2]
    symbol1 = str(sys.argv[3])
    symbol2 = str(sys.argv[4])
    filter(inFilenames, outFilename, symbol1, symbol2)


if __name__ == '__main__':
    _main()

