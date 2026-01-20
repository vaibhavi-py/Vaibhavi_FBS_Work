# Python Program to Check if a Given Key Exists in a Dictionary or Not

my_dict = {"name": "Amit", "age": 22, "city": "Mumbai"}

key = input("Enter key to check: ")

if my_dict.get(key) is not None:
    print(f"Key '{key}' exists in the dictionary")
else:
    print(f"Key '{key}' does not exist in the dictionary")
