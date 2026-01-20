# Python Program to Multiply All the Items in a Dictionary

my_dict = {"a": 2, "b": 3, "c": 4}

product = 1  # Start with 1 because multiplying by 0 gives 0

for value in my_dict.values():
    product *= value

print("Product of all dictionary values:", product)
