## Python Program to Sort the List According to the Second Element in Sublist


data = [[1, 3], [4, 1], [2, 2], [5, 0]]

data.sort(key=lambda x: x[1])

print(data)
