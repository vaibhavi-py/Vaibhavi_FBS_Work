## WAP TO CHECK WHETHER THE USER HAS ENTERED THE CORRECT USER ID AND PASSWORD.

userid = ('Vaibhavi')
password = ('2004')

uid = input("Enter the User ID :",)
pwd = input("Enter the password:",)

if(uid==userid and pwd==password):
    print("Login Successful.")
else:
    print("invalid user ID and password.")
    