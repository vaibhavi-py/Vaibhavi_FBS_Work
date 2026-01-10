## Write a program to create three lists of numbers, their squares
# and cubes

# Input number of elements
n = int(input("Enter how many numbers you want: "))

# Initialize lists
numbers = []
squares = []
cubes = []

# Create the lists
for i in range(1, n + 1):
    numbers.append(i)
    squares.append(i ** 2)
    cubes.append(i ** 3)

# Print the lists
print("Numbers List:", numbers)
print("Squares List:", squares)
print("Cubes List:", cubes)



