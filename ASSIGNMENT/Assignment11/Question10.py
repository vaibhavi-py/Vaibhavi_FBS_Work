## Write a program to print list after removing even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
for n in numbers:
    if n % 2 != 0:
        count += 1

odd_numbers = [0] * count
index = 0

for n in numbers:
    if n % 2 != 0:
        odd_numbers[index] = n
        index += 1

print("List after removing even numbers:", odd_numbers)
