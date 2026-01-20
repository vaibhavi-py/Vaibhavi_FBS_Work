# Write a Python program to find all the anagrams and group them
#together from a given list of strings.

# List of strings
words = ["listen", "silent", "enlist", "hello", "ohlle", "world"]

# Dictionary to group anagrams
anagram_groups = {}

for word in words:
    # Sort the word and use as key
    key = ''.join(sorted(word))
    if key in anagram_groups:
        anagram_groups[key].append(word)
    else:
        anagram_groups[key] = [word]

# Display anagram groups
print("Grouped Anagrams:")
for group in anagram_groups.values():
    print(group)
