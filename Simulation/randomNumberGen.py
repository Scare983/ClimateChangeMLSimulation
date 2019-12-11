import random
import sys
# this file takes in one number to create a random value from.
#change seed value here for different random generation.
random.seed(1)
# so pick a random number between o and 1.5* given input.
print(sys.argv[1])
print(float(random.uniform(0, float(sys.argv[1]) * 1.5 )))