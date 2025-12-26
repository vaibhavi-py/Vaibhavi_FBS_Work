## WAP TO CHECK IF GIVEN NUMBER IS STRONG NUMBER .
# Strong number is a number whose sum of factorials of its digits is equal to the number itself.

n = int(input("Enter a number :"))
temp = n
sum_of_Factorial = 0

for digit in str(n):
    fact = 1
    for i in range(1, int(digit)+1):
        fact *= i
    sum_of_Factorial += fact

if (sum_of_Factorial == n):
    print(n, "is a strong number")
else:
    print(n, "is Not a strong number")
    