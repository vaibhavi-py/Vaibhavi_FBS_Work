## WAP TO CHECK IF THE GIVIEN NUMBER IS A PERFECT NUMBER .
# perfect number = a number which is a positive integer that equals the sum of its proper divisor excluding the number itself .

# n = 6 .

n = int(input("Enter a number :"))
sum_of_divisor = 0
i = 1

while(i<n):
    if (n % i == 0):
        sum_of_divisor += i 
    i = 1 + i 

if (sum_of_divisor == n):
    print(n, "is a Perfect Number")
else :
    print(n, "is Not a Perfect Number")