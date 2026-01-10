## Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list.

numbers = [10, 20, 30, 20, 40, 20, 50]

key = int(input("Enter the number to search: "))

count = 0

for num in numbers:
    if num == key:
        count += 1

if count > 0:
    print(key, "is present in the list")
    print("It is present", count, "times")
else:
    print(key, "is not present in the list")
