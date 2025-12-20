## CONVERT DISTANT GIVEN IN FEET AND INCHES INTO METERS AND CENTIMETERS.

feet = 5
inches = 6

feet = int(input("enter feet:",))
inches = int(input("enter inches:",))

meters = (feet * 0.3048) + (inches * 0.0254)

centimeters= (meters * 100)
 
print("Meters:",meters)
print("Centimeters:",centimeters)
