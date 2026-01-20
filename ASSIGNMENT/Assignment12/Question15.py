# Python Program to find larger string without using built-in functions.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

count1 = 0
count2 = 0

# Count characters in first string
for ch in str1:
    count1 += 1

# Count characters in second string
for ch in str2:
    count2 += 1

if count1 > count2:
    print("Larger string:", str1)
elif count2 > count1:
    print("Larger string:", str2)
else:
    print("Both strings are of equal length")
