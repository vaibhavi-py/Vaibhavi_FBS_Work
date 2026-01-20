# Python Program to Count the Number of Vowels in a String

string = input("Enter a string: ")
count = 0

vowels = "aeiouAEIOU"

for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
