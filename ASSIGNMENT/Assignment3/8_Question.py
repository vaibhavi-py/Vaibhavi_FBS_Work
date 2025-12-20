## PROGRAM TO PROMPT USER TO ENTER USER IF AND PASSWORD. AFTER VERIFYING USERID AND PASSWORD DISPLAY A 4 DIGIT RANDOM NUMBER AND ASK USER TO ENTER THE SAME. IF USER ENTERS THE SAME NUMBER THEN SHOW HIM SUCCESS MESSAGE OTHERWISE FAILED

import random 

correct_userid = "Vaibhavi"
correct_password = "2004"

# TAKE INPUT FROM USER
userid = input("Enter the User ID :",)
password= input("Enter the Password :",)
    
# TO VERIFY USER ID AND PASSWORD.
if(userid == correct_userid and password == correct_password):
    print("Login Successful.")

# TO GENERATE 4 DIGIT RANDOM NUMBER. (CAPTCHA) TAKE IT FROM USER.
import random
captcha = random.randint(1111, 9999)
print("Captcha:", captcha)

# ASK USER TO ENTER CAPTCHA.
user_captcha = int(input('Enter the captcha :',))

#TO VERIFY CAPTCHA 
if(user_captcha == captcha):
    print("Verification Successful !! .")

else:
    print("Something Went Wrong Try Again !! .")



