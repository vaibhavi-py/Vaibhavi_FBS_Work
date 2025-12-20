##WAP TO CALCULATE PERCENTAGE OF STUDENT BASED ON BEST OF FIVE CRITERIA

#Take Input

a= int(input('english subject:',))
b= int(input('maths subject:',))
c= int(input('hindi subject:',))
d= int(input('marathi subject:',))
e= int(input('history subject:',))

total_marks = (a+b+c+d+e)
percentage = (total_marks/500)*100

print("Total Marks :", total_marks)
print("percentage :",percentage, '%')












