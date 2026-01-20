## Python Program to Find the Second Largest Number in a List Using Bubble
#Sort

numbers = [12, 35, 1, 10, 34, 1]

n = len(numbers)

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# Second largest element
second_largest = numbers[n - 2]

print("Second Largest Number:", second_largest)
