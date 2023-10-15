
import random

# Generating a list of 20 random integers in the range [0, 100]
numbers = [random.randint(0, 100) for _ in range(20)]

# Printing all numbers that are at least 85
for num in numbers:
    if num >= 85:
        print(num)
