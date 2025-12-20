## WAP TO INPUT ELECTRICITY UNIT CHARGES AND CALCULATE TOTAL ELECTRICITY BILL .

#1 50 units rs 0.50/unit
#2 100 units rs 0.75/unit
#3 100 units rs 1.20/unit
#4 above 250 rs 1.50/ units
# additional subcharge of 20% is added to the bill. 

unit = int(input("Enter the unit consumed:",))

if(unit<=50):
    bill= unit * 0.50 
elif(unit<=150):
    bill = 50 * 0.50 + (unit-50)*0.75
elif(unit<=250):
    bill = (50 * 0.50) + (100 * 0.75) + (unit-150) * 1.20
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (unit - 250) * 1.50

bill = bill + bill*0.20   #subcharge 
print("Total Bill = ", bill)