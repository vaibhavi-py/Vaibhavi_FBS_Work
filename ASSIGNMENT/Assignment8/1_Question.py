## WAP TO CALCULATE AREA OF RECTANGLE USING FUNCTON.

# function to calculate area

def rectangle_area(length, breadth):
    return length * breadth

# input from user

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

# calculate area

area = rectangle_area(length, breadth)

print("The area of the rectangle is:", area)
