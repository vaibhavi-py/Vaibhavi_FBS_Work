# WAP A PROGRAM TO FIND SUM OF FOLLOWING SERIES USING RECURSIVE FUNCTION: 
# 1! + 2! + 3! +4!+...+ n! 
# FOR FACT AND SUM TWO RECURSIVE FUNCTIONS.

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def sum_series(n):
    if n == 1:
        return fact(1)
    return fact(n) + sum_series(n - 1)

# Main program
n = int(input("Enter value of n: "))
result = sum_series(n)
print("Sum of the series is:", result)
