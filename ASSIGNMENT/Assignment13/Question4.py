# Python Program to Generate a Dictionary that Contains Numbers (between 1
#and n) in the Form (x,x*x).


n = int(input("Enter a number: "))

squares_dict = {}

for x in range(1, n+1):
    squares_dict[x] = x * x

print("Generated dictionary:", squares_dict)
