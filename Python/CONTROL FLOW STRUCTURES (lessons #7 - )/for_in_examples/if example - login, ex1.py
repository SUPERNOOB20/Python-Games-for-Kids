real_username = "Valen"
real_password = "12345"

attempt_username = input("Please enter your username.")
attempt_passowrd = input("Please enter your password.")

if (real_username == attempt_username and real_password == attempt_passowrd):
    print("ok you're in :D")
else:
    print("error: try again!")

print("the rest of the program")