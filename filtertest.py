import sys
import stdio
import fileinput

sigma = sys.argv[1]

while not stdio.isEmpty():
 # Process one integer.
 value = stdio.readFloat()
 if value >= 1.5*sigma:
     stdio.write(str(value) + ' ')
stdio.writeln()