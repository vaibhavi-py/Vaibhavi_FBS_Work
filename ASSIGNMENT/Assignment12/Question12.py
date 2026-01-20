# Python Program to count number of lowercase characters in a string.

string = input("Enter a string: ")
count = 0

for ch in string:
    if ch.islower():
        count += 1

print("Number of lowercase characters:", count)
