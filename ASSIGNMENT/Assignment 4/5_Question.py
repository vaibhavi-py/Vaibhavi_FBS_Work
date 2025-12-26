## WAP TO PRINT FIBONACCI SERIES UPTO 'n' . (for loop)

#Fibonacci series begins with 0 and 1 . 
#add to previous numbers to get the next one . 

n = 5
a = 0
b = 1

n = int(input("Enter the number :"))
for i in range(n):
    print(a, end="" )
    c = a +b
    a = b
    b = c 