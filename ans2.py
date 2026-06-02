correct_username = "shubha"
correct_password = "3658"

for i in range(3):
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == correct_username and p == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Credentials")

else:
    print("Account Locked")