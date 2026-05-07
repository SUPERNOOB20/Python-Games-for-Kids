registered_username = "Azu"
registered_password = "i_like_cheese"


print("Welcome to Netfleece!")
attempted_username = input("Enter your username\n")
attempted_password = input("Enter your password\n")

if (registered_username == attempted_username and registered_password == attempted_password):
    print("logged in succesfully :)")

else:
    if registered_username != attempted_username:
        print("WRONG USERNAME! Try again!")
    else: # if the passwords are not the same
        print("WRONG PASSWORD! Try again!")



