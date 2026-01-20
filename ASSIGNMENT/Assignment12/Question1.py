## Python Program to Replace all Occurrences of ‘a’ with $ in a String

string = input("Enter a string: ")
new_string = ""

for ch in string:
    if ch == 'a':
        new_string += '$'
    else:
        new_string += ch

print("Updated string:", new_string)
