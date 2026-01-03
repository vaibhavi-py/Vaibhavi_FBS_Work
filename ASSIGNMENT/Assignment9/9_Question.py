# WAP TO CALCULATE THE m TO THE POWER OF n USING RECURSION FUNCTION.

# Recursive function to calculate m^n
def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

# Main program
m = int(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))

result = power(m, n)
print(f"{m} to the power of {n} is: {result}")
