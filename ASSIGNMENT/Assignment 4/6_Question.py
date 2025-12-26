## WAP TO CHECK IF A GIVEN NUMBER IS PRIME OR NOT . (Using for loop )
# PRIME NUMBER : a number that can be divided by only itself . 

# n = 7

n = int(input("Enter Number :" ))

for i in range (2,n):
    print(i)
    if(n % i == 0):
        print(f'{n} is not a prime number .')
        break 

else:
    print(f'{n} is a prime number .')
