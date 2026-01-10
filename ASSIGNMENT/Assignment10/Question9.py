# Write a program to remove all occurrences of a given element in the list.

# Sample list
numbers = [1, 2, 3, 2, 4, 2, 5]

# Element to remove
element_to_remove = int(input("Enter the element you want to remove: "))

# Remove all occurrences
while element_to_remove in numbers:
    numbers.remove(element_to_remove)

# Print the updated list
print("List after removing", element_to_remove, ":", numbers)
