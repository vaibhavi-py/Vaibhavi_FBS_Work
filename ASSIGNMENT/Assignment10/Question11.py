## Write a program to print list after removing even numbers.

# Input list from user
n = int(input("Enter the number of elements in the list: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Remove even numbers using a new list
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the result
print("List after removing even numbers:", odd_numbers)


