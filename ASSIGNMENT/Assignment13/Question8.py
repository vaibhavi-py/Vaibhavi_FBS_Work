# Python Program to Count the Frequency of Words Appearing in a String Using
#a Dictionary

string = input("Enter a string: ")

# Split the string into words
words = string.split()

# Initialize an empty dictionary
word_freq = {}

# Count the frequency of each word
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Display word frequencies
print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"{word} : {freq}")
