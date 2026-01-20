## Python Program to Put Even and Odd elements of a List into two Different
#Lists


numbers = [10, 15, 20, 25, 30, 35]

even = [0] * len(numbers)
odd = [0] * len(numbers)

e = 0
o = 0

for num in numbers:
    if num % 2 == 0:
        even[e] = num
        e += 1
    else:
        odd[o] = num
        o += 1

print("Even elements:")
for i in range(e):
    print(even[i])

print("Odd elements:")
for i in range(o):
    print(odd[i])
