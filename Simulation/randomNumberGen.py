import random
import sys
# this file takes in one number to create a random value from.
#change seed value here for different random generation.

with open('RandomSeedValue.txt') as f:
    value = f.readline()
random.seed(value)
# so pick a random number between o and 1.5* given input.
print(float(random.uniform(0, float(sys.argv[1]) * 1.5 )))
