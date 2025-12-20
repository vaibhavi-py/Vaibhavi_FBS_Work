## WAP TO CHECK IF GIVEN 3 DIGIT NUMBER IS A PALINDROME OR NOT.

#Palindrome = it is a word, number that reads the same backwards as forwards.
# rev = reverse of the number.
# temp = temporary number.

num = int(input('Enter a 3 digit number :'))

rev = 0
temp = num 

while(temp>0):
    r = temp % 10  
    rev = rev * 10 + r 
    temp = temp // 10

if (num == rev):
    print("Palindrome number.")
else:
    print("Not a palindrome number.")
