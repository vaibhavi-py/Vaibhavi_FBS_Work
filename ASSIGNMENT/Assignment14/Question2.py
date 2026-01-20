# Write a Python program to remove the intersection of a second set
#with a first set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Elements in set1 not in set2
result = set1 - set2

print("Set after removing intersection:", result)
