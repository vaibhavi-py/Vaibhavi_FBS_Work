## Python Program to Form a New String where the First Character and
#the Last Character have been Exchanged

str1 = input("Enter the string= ",)
print("Original string = ",str1)
newstr=""

for i in range(len(str1)):
    if i == 0:
        newstr += str1[-1]
    elif i ==len(str1)-1:
        newstr += str1[0]
    else:
        newstr+=str1[i]

print("New string=", newstr)