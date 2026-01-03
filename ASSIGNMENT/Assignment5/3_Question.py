## wap to print armstrong number within given range 

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong numbers between", start , "and" , end , "are :")

for num in range(start , end+1):
    temp = num
    digits = len(str(num))
    sum = 0

    while (temp > 0) :
        digit = temp % 10
        sum = sum + digit ** digits
        temp = temp // 10

    
    if (sum == num):
        print(num)