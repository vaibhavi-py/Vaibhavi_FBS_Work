#WAP TO CHECK THE GIVEN NUMBER IS PRIME OR NOT USING RECURSIVE FUNCTION.


def is_prime_recursive(num, i=2):
    if num < 2:
        return False
    if i > num // 2:
        return True
    if num % i == 0:
        return False
    return is_prime_recursive(num, i + 1)

# Main program
n = int(input("Enter a number: "))

if is_prime_recursive(n):
    print(n, "is a Prime number")
else:
    print(n, "is Not a Prime number")
