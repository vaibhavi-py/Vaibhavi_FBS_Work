## WAP TO PRINT SUM OF SERIES UPTO 'n' . (using for loop .)

# series = 1+2+3+...+n

n = int(input("Enter the number :"))

sum = 0
for i in range (1,n+1):
    sum = sum + i
    print("Sum of series = ", sum )

