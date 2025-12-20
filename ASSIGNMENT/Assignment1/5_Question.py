##WAP TO ENTER P.T.R AND CALCULATE COMPOUND INTEREST

#Take Input

p= int(input('enter principle value:',))
r= int(input('enter rate:',))
t= int(input('enter time:',))

ci= p*(1+r/100)*2-p

print('Compund Interest will be :', ci)