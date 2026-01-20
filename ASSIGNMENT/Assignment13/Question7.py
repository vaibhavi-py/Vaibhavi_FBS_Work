# Python Program to Remove the Given Key from a Dictionary


my_dict = {"name": "Amit", "age": 22, "city": "Mumbai"}

key_to_remove = input("Enter key to remove: ")

if key_to_remove in my_dict:
    my_dict.pop(key_to_remove)
    print("Updated dictionary:", my_dict)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary")
