# Write a Python program to find the two numbers whose product is
#maximum among all the pairs in a given list of numbers. Use the
#Python set.


# Given list of numbers
nums = [1, -10, -20, 5, 3, 2]

# Convert list to set to remove duplicates (optional)
num_set = set(nums)

max_product = None
pair = ()

num_list = list(num_set)  # Convert set back to list for indexing

# Check all pairs
for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        product = num_list[i] * num_list[j]
        if (max_product is None) or (product > max_product):
            max_product = product
            pair = (num_list[i], num_list[j])

print(f"The pair with maximum product is {pair} with product {max_product}")
