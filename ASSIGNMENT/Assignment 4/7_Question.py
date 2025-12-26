## WAP TO PRINT ALL INTEGERS UPTO 'n' THAT ARE NOT DIVISIBLE BY 2 AND 3 .

#n=10

n = int(input("Enter a number :"))

for i in range(1, n+1):
    if (i % 2 !=0 and i % 3 !=0):
        print(i, end = " ")
    
