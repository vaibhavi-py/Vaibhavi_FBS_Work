## WAP TO PRINT ALL NUMBERS IN A RANGE DIVISIBLE BY A GIVEN NUMBER

start = int(input("Enter starting number :"))
end = int(input("Enter ending number :"))
divisor = int(input("Enter the number to check divisiblity :"))

i = start 
while (i<=end):
    if (i % divisor == 0):
        print(i)
    i = i + 1 