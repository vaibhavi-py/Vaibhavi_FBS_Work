# Write a Python program to find all the unique combinations of 3
#numbers from a given list of numbers, adding up to a target number.

from itertools import combinations

# Input list and target sum
nums = [1, 2, 3, 4, 5, 6]
target = 10

# Find all unique combinations of 3 numbers
combos = [combo for combo in combinations(nums, 3) if sum(combo) == target]

print(f"Combinations of 3 numbers that sum to {target}:")
for combo in combos:
    print(combo)
