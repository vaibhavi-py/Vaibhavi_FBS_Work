## Write a program to create three lists of numbers, their squares and cubes


n = 5

numbers = [0] * n
squares = [0] * n
cubes = [0] * n

for i in range(n):
    numbers[i] = i + 1
    squares[i] = (i + 1) * (i + 1)
    cubes[i] = (i + 1) * (i + 1) * (i + 1)

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
