## WAP TO INPUT ALL SIDES OF A TRIANGLE AND CHECK WHEATHER TRIANGLE IS VALID OR NOT.

a = int(input('Enter first side:',))
b = int(input('Enter second side:',))
c = int(input('Enter third side:',))

if(a>0 and b>0 and c>0 and (a+b>c) and (a+c>b) and (b+c>a)):
    print('Triangle is valid.')
else:
    print('Triangle is not valid')