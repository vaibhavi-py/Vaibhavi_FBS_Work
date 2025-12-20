## program to convert days into years, weeks and days

givendays = int(input('enter number of days:',))

years=givendays//365
 
weeks=(givendays%365)//7

days= givendays-(365*years)-(7*weeks)



print('years:' + str(years))

print('weeks:'+ str(weeks))

print('days:'+ str(days))




 