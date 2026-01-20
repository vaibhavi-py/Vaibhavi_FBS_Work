# Python Program to Concatenate Two Dictionaries Into One

dict1 = {"name": "Amit", "age": 22}
dict2 = {"city": "Mumbai", "profession": "Student"}

merged_dict = dict1.copy()  # Make a copy of dict1

for key in dict2:
    merged_dict[key] = dict2[key]

print("Merged dictionary:", merged_dict)
