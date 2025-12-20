## REVERSE THREE DIGIT NUMBERS.

num = 123

num = int(input('enter the three digit number:',))

a = num // 100
b = (num//10) % 10
c = num % 10

reverse = c * 100 + b * 10 + a

print("reversed number=", reverse )
