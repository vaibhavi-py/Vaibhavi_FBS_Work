## WAP TO CHECK IF PERSON IS ELIGIBLE TO MARRY OR NOT (MALE AGE >= 21 AND FEMAL AGE >=18)

gender = input('Enter the gender (M/F) :',)
age = int(input('Enter the age :',))

if(gender=='M'):
    if(age>=21):
        print("person is eligible for marriage.")
    else:
        print("person is not eligible for marriage.")

else:
    if(age>=18):
        print("person is eligible for marriage.")
    else: 
        print("person is not eligible for marriage.")