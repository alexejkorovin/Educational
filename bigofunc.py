import stdio
import stopwatch
import matplotlib.pyplot as plt

def calculate(n):
    c = [[0 for x in range(n)] for y in range(n)]
    timer = stopwatch.Stopwatch()
    for i in range(n):
        for j in range(n):
            if i == j:
                c[i][j] = 1.0
            else:
                c[i][j] = 0.0
    elapsed = timer.elapsedTime()
    # freq = 1.0E9 * elapsed / float(n) / float(n)
    # stdio.writef('%7.1f: %s\n', freq, '2d array operation 2-for loops 1-if')
    return elapsed / float(n)

def f(n):
    if (n == 0): return 1
    return f(n-1) + f(n-1)

inputv = [0]*3000
timev = [0]*3000

for i in range(1,15):
    inputv[i] += i
    timev[i] += f(i)

plt.plot(inputv,timev, color='red', marker='o')
plt.title('Big O', fontsize=14)
plt.xlabel('Input', fontsize=14)
plt.ylabel('Time', fontsize=14)
plt.grid(True)
plt.show()