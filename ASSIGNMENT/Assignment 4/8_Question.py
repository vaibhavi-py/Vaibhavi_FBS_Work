## WAP TO FIND WHICH NUMBERS ARE DIVISIBLE BY 7 AND MULTIPLE OF 5 WITH A GIVEN RANGE.

#start no : 1 
#end no : 100

start = int(input("Enter the starting number :"))
end = int(input("Enter the ending number :"))

print("Number divisible by 7 and multiple of 5 in the given range :")


for i in range(start , end + 1):
    if (i % 7 == 0 and i % 5 == 0):
        print(i, end="")


