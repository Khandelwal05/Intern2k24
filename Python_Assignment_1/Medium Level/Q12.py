name=input("Enter Username here: ")
password= input("Enter password here ")
password2=input("Enter your password again to recheck ")


for i in range (3):
    if (password!= password2):
        password2=input("Enter your password again here ")
        print("Incorrect password")
    else :
        print("Log in successful")
        break