# Write a Python program to find all the unique words and count the
#frequency of occurrence from a given list of strings. Use Python set
#data type.

# List of strings
string_list = [
    "python is easy",
    "python is powerful",
    "learning python is fun"
]

# Step 1: Create an empty list to store all words
all_words = []

# Step 2: Split each string into words and add to the list
for sentence in string_list:
    words = sentence.split()
    all_words.extend(words)

# Step 3: Convert list to set to get unique words
unique_words = set(all_words)

# Step 4: Count frequency of each unique word
print("Word frequencies:")
for word in unique_words:
    frequency = all_words.count(word)
    print(f"{word} : {frequency}")
