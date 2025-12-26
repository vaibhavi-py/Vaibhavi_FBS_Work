## WAP TO PRINT FACTORIAL OF NUMBER . (Using while loop .)

num = int(input("Enter the number :"))
fact = 1  #because factorial multiplication starts with 1 
i = 1

while(i<=num):
    fact = fact*i
    i = i + 1
print(f"Factorial of {num} = {fact}")
