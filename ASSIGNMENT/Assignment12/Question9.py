# Python Program to Calculate the Number of Words and the Number of
#Characters Present in a String


string = input("Enter a string: ")

char_count = len(string)
word_count = len(string.split())

print("Number of characters:", char_count)
print("Number of words:", word_count)
