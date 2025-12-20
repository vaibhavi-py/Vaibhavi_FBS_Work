## WAP TO CHECK WHETHER THE TRIANGLE IS EQUILATERAL, ISOOCELES OR SCALENE.

# EQUILATERAL TRIANGLE : ALL THREE SIDES ARE EQUAL.
# ISOSCELES TRIANGLE : ANY TWO SIDES ARE EQUAL.
# SCALENE : ALL THREE SIDES ARE DIFFERENT.

a = int(input('Enter first side:'))
b = int(input('Enter second side:'))
c = int(input('Enter third side:'))

if(a==b and b==c):
    print("Equilateral Triangle.")

elif(a==b and b==c and c==a):
    print("Isosceles Triangle.")
    
else:
    print("Scalene Triangle.")