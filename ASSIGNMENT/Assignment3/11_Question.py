## ACCEPT AGE OF FIVE PEOPLE AND ALSO PER PERSON TICKET AMOUNT AND THEN CALCULATE TOTAL AMOUNT TO TICKET TO TRAVEL FOR ALL OF THEM BASED ON FOLLWING CONDITION:
# a) Children below 12 = 30% discount 
# b) Senior citizen (Above 59) = 50 % discount 
# c) Others need to pay full .

total = 0


age = int(input('Enter Age :',))
ticket = int(input('Enter Ticket Amount :',))

 
if(age<12):
    ticket = ticket - ticket * 30 / 100
    total = total + ticket

elif(age>59):
    ticket = ticket - ticket * 50 / 100
    total = total + ticket
 
print("Total ticket amount =", total)




    