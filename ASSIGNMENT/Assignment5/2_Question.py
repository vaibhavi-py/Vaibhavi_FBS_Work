## Children below 12 = 30% discount 
# Senior citizen (above 59) = 50% discount 
# other need to pay full

n = int (input ("Enter number of passengers: "))

ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0

for i in range (1,n+1):
    age = int(input(f"Enter age of passanger {i} : "))

    if (age < 12):
        fare = ticket_cost * 0.70   #30%
    
    elif (age>58):
        fare = ticket_cost * 0.50

    else:
        fare = ticket_cost 
    
    total_amount += fare 

print("Total ticket amount to be paid =" , total_amount)