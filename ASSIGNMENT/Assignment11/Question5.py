## Python Program to Sort a List According to the Length of the Elements
#within the list.


words = ["apple", "kiwi", "banana", "fig", "grapes"]

n = len(words)

for i in range(n):
    for j in range(i + 1, n):
        if len(words[i]) > len(words[j]):
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

print(words)
