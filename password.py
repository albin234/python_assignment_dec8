Global_password='kathmandu'

def psw():
    password=str(input("enter the password"))

    if password==Global_password:
        print("correct paasword")

    else:
        print("incorrect password")

psw()