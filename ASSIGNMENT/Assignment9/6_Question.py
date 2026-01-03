# WAP TO PRINT FIBONACCI SERIES USING RECURSIVE FUNCTION.

# Recursive function to find nth Fibonacci number
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Main program
n = int(input("Enter number : "))

print("Fibonacci series:")
for i in range(1, n + 1):
    print(fibonacci(i), end=" ")
