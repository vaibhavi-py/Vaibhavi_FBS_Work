## Python Program to Merge Two Lists and Sort it


list1 = [4, 1, 7]
list2 = [3, 9, 2]

merged = [0] * (len(list1) + len(list2))
k = 0

# Copy list1 elements
for i in range(len(list1)):
    merged[k] = list1[i]
    k += 1

# Copy list2 elements
for i in range(len(list2)):
    merged[k] = list2[i]
    k += 1

# Sorting logic (ascending order)
for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            temp = merged[i]
            merged[i] = merged[j]
            merged[j] = temp

print("Merged and Sorted List:", merged)
