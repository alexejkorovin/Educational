

import random
import sys
import numpy

roll_count = int(sys.argv[1])
target = int(sys.argv[2])
threshold = int(sys.argv[3])
test_count = 100000 # magic numbers bad!
threshold_met = 0

for _ in range(test_count):

    target_count = 0
    for _ in range(roll_count):
        roll = random.randint(1, 6)
        if roll == target:
            target_count += 1
    if target_count >= threshold:  # if the threshold is met
        threshold_met += 1

probability = threshold_met / test_count
print(probability)







