# Write a Python program that finds all pairs of elements in a list whose
#sum is equal to a given value.

# Input list and target sum
nums = [1, 2, 3, 4, 5, 6, 7]
target = 7

# Find pairs
pairs = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

print(f"Pairs whose sum is {target}:", pairs)
