# WAP TO CHECK IF ENTERED NUMBER IS PALINDROME OR NOT USING FUNCTION .

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if is_palindrome(n):
    print("The number is a Palindrome")
else:
    print("The number is Not a Palindrome")
