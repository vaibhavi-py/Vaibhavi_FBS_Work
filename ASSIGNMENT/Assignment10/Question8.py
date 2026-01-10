## Write a program to create a duplicate of an existing list. It should not point to
# same list.

# Original list
original_list = [1, 2, 3, 4, 5]

# Method 1: Using list slicing
duplicate_list1 = original_list[:]

# Method 2: Using the list() function
duplicate_list2 = list(original_list)

# Method 3: Using the copy() method
duplicate_list3 = original_list.copy()

# Print all lists
print("Original List:", original_list)
print("Duplicate List 1:", duplicate_list1)
print("Duplicate List 2:", duplicate_list2)
print("Duplicate List 3:", duplicate_list3)

# Modify duplicate to show independence
duplicate_list1.append(6)
print("\nAfter modifying duplicate_list1:")
print("Original List:", original_list)
print("Duplicate List 1:", duplicate_list1)
