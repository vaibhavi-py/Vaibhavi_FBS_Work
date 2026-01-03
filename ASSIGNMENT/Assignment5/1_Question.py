## WAP TO PROMPT USER TO ENTER USER ID AND PASSWORD. IG ID AND PASSWORD IS INCORRECT GIVE HIM CHANCE TO RE-ENTER THE CREDENTIALS . LET HIM TRY 3 TIMES . AFTER THAT PROGRAM TO TERNIMATE .

correct_userid = "Admin"
correct_password = "1234"

attempts = 0 

while (attempts <3):
    userid =  input("Enter User Id :")
    password = input("Enter password :")

    if(userid == correct_userid and password == correct_password):
        print('Login Successful')
        break 

    else :
        attempts += 1
        print('Invalid User Id or Password')

        print('Attempts left:', 3 - attempts)

if (attempts == 3):
    print("Account locked. program terminated")