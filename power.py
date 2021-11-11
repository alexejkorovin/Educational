import stdio
import sys
powern = int(sys.argv[1])
i = 0
power = 1
stdio.writeln(str(i) + ' ' + str(power))
while powern > 2*power:
 power = 2*power
 i+=1
 stdio.writeln(str(i) + ' ' + str(power))

