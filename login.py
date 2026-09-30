#project should contain a username and password
#A user is given 5 attempts to try and login else user is blocked from accessing


username = "Abbiemma"
passwrd = "Abby@emma"
trials=0

new_username=""
new_passwrd=""

while trials<=5:
    new_username=input("Please enter your username:")
    new_passwrd=input("Enter your password:")
    if (new_username == username) & (new_passwrd == passwrd):
        trials = 0
    elif (username!=new_username) | (passwrd!=new_passwrd):
        trials+=1
    else:
        trials=6



    if trials==0:
        print("you are successfully logged in!")
        break


    elif trials<=5:
        print("Username or Password do not match,please try again")

    elif trials==6:
        print("You have been blocked!!!")
        break
    else:
        break

















