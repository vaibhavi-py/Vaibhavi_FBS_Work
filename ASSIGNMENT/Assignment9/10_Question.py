# WAP TO REVERSE NUMBER USING RECURSIVE FUNCTION.

# Recursive function to reverse a number
def reverse_number(num, rev=0):
    if num == 0:
        return rev
    rev = rev * 10 + num % 10
    return reverse_number(num // 10, rev)

# Main program
n = int(input("Enter a number: "))
reversed_num = reverse_number(n)
print("Reversed number is:", reversed_num)
