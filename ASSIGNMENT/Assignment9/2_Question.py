# WAP TO CHECK IG GIVEN NUMBER IS ARMSTRONG OR NOT USING RECURSIVE FUNCTION.

# Recursive function to count digits
def count_digits(num):
    if num == 0:
        return 0
    return 1 + count_digits(num // 10)

# Recursive function to calculate sum of digits raised to power 'digits'
def armstrong_sum(num, digits):
    if num == 0:
        return 0
    return (num % 10) ** digits + armstrong_sum(num // 10, digits)

# Function to check Armstrong
def is_armstrong(num):
    digits = count_digits(num)
    return num == armstrong_sum(num, digits)

# Main program
n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is Not an Armstrong number")
