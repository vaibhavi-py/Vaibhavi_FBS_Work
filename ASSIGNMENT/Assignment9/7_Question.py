# WAP TO FIND SUM OF DIGITS USING RECURSIVE FUNCTION.

# Recursive function to find sum of digits
def sum_of_digits(num):
    if num == 0:
        return 0
    return (num % 10) + sum_of_digits(num // 10)

# Main program
n = int(input("Enter a number: "))
result = sum_of_digits(n)
print("Sum of digits is:", result)
