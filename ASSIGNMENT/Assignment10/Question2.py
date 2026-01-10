## Write a program to find maximum and minimum element in a list.


numbers = [25, 10, 45, 5, 30]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum element:", max_num)
print("Minimum element:", min_num)
