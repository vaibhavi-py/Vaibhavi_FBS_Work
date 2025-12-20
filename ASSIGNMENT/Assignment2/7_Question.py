## FIND SUM OF THREE DIGIT NUMBER.

num= 345

num= int(input("enter the three digit number:",))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum_digits = a + b + c 

print ("sum of digits =", sum_digits)