# WAP TO CHECK IF A GIVEN NUMBER IS ARMSTRONG OR NOT. FOR EACH TASK CREATE SEPARATE FUNCTIONS

def count_digits(num):
    return len(str(num))

def armstrong_sum(num, digits):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total

def is_armstrong(num):
    digits = count_digits(num)
    return num == armstrong_sum(num, digits)

# Main program
n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is Not an Armstrong number")
