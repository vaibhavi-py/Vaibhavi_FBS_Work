# WAP TO FIND SUM OF N NUMBER USING FUNCTIONS.

def sum_of_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Main program
n = int(input("Enter a number: "))
result = sum_of_n(n)
print("Sum of first", n, "numbers is:", result)
