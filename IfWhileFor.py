import stdio
import sys
n = int(sys.argv[1])

stdio.writeln('If')

if n > 0:
    stdio.writeln('n > 0')
else:
    stdio.writeln('n < =0')

stdio.writeln('For')
for i in range(1, 10):
    stdio.writeln('n <= 0')

stdio.writeln('While')
while True:
    num = input("Enter finish:")
    if num == "finish":  # Type 'finish' to get the output
        break

    if n > 0:
        stdio.writeln('n > 0')
    elif n <= 0:
        stdio.writeln('n <= 0')


stdio.writeln('n <= 0')