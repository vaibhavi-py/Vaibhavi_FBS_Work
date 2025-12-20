## CALCULATE SELLING PRICE OF BOOK AND COST PRICE AND DISCOUNT

cost_price= int(input('enter cost price:',))
discount= int(input('enter discount:',))

discount_amount= (discount/100)*cost_price

print("Discount amount will be :",discount_amount)

# for selling price 

selling_price= cost_price - discount_amount

print("Selling Price will be :",selling_price)
