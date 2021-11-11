import sys
import math
import stdarray
import stddraw
import random
import stdstats
import gaussian

n = int(sys.argv[1])  # population

vote_a = 0.51
vote_b = 0.49
mistake = 0.05
result_A = 0
result_B = 0
result_mistake = 0
for i in range(n):
    test = random.random()
    if test < vote_a: result_A += 1
    if test > vote_a: result_B += 1
    if test < mistake: result_mistake += 1
print('A '+str(result_A))
print('B '+str(result_B))
print('Mistake '+str(result_mistake))