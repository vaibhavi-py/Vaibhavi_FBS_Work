# 13. Python Program to count number of digits and letters in a string.

string = input("Enter a string: ")

letters = 0
digits = 0

for ch in string:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        letters += 1
    elif '0' <= ch <= '9':
        digits += 1

print("Number of letters:", letters)
print("Number of digits:", digits)
