# WAP TO CALCULATE AREA OF CIRCLE USING FUNCTON.


import math  # to use pi

# function to calculate area
def circle_area(radius):
    return math.pi * radius * radius

# input from user
radius = float(input("Enter the radius of the circle: "))

# calculate area
area = circle_area(radius)

print("The area of the circle is:", area)
