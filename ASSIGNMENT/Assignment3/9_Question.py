## INPUT 5 SUBJECT MARKS FROM USER AND DISPLAY GRADE (EG. FIRST CLASS, SENCOND CLASS.)

# INPUT MARKS OF 5 SUBJECTS . 
m1 = int(input("Enter marks of subject 1 : ",))
m2 = int(input("Enter marks of subject 2 :",))
m3 = int(input("Enter marks of subject 3 :",))
m4 = int(input("Enter marks of subject 4 :"))
m5 = int(input("Enter marks of subject 5 :",))

# CALCULATE TOTAL AND PERCENTAGE.
total= m1+m2+m3+m4+m5
percentage= total / 5

print("total:" , total)
print("percentage :" , percentage, '%')


# FOR CHECKING GRADE .

if(percentage>=60):
    print("Grade : First Class.")
elif(percentage>=50):
    print("Grade : Second Class.")
elif(percentage>=40):
    print("Grade : Pass Class.")
else:
    print("Grade : Fail.")