##WAP FIND ROOTS OF QUADRATIC EQUATION

#Take Input

a= int(input("Enter a :"))
b= int(input("Enter b :"))
c= int(input("Enter c :"))

#apply formula.

d = (b*b-4*a*c)
print('D=', d)

#Quadratic Equation 
r1 = (-b+(0.5*d))/(2*a)
r2 = (-b-(0.5*d))/(2*a)

print("Root 1 = ", r1)
print("Root 2 =", r2)