## Write a program to reverse the list.

numbers = [10, 20, 30, 40, 50]

rev_list = []

for i in range(len(numbers) - 1, -1, -1):
    rev_list.append(numbers[i])

print("Reversed list:", rev_list)
