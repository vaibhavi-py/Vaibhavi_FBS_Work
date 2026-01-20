# Write a Python program to find the longest common prefix of all
#strings. Use the Python set.

# List of strings
string_list = ["flower", "flow", "flight"]

if not string_list:
    print("Empty list, no common prefix")
else:
    # Take the first string as reference
    first_str = string_list[0]
    prefix = ""

    for i in range(len(first_str)):
        # Collect all characters at position i from all strings
        char_set = set(s[i] for s in string_list if i < len(s))

        # If all characters are the same, it will have length 1
        if len(char_set) == 1:
            prefix += first_str[i]
        else:
            break

    print("Longest common prefix:", prefix)
