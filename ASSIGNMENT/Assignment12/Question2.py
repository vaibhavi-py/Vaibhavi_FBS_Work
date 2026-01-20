## Python Program to Remove the nth Index Character from a Non-Empty
#String

string = input("Enter a string: ")
n = int(input("Enter index to remove: "))

new_string = ""

for i in range(len(string)):
    if i != n:
        new_string += string[i]

print("String after removal:", new_string)
