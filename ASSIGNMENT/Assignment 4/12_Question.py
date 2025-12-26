## WAP TO CHECK IF GIVEN NUMBER IS ARMSTRONG NUMBER OR NOT.
# An armstrong number is a number whose sum of the powers of its digits equal to number its self.
# input = 153 . 


n = int(input("Enter a number :"))
sum_of_powers = 0
num_digits = len(str(n))

for digit in str(n):
    sum_of_powers += int(digit) ** num_digits

if (sum_of_powers == n):
    print(n,"is an Armstrong Number .")
else:
    print(n, "is Not a Armstrong Number .")
