balance = 100
exit    = False

print("Welcome to Royal Bank Ltd.")

while exit == False:
    operation = input("Choose an operation:\n  1) Deposit. \n 2) Withdraw. \n 3) Check balance. \n 4) Exit. \n")

    if operation == "1":
        balance = balance + int(input("How much do you want to deposit?\n"))

    elif operation == "2":
        withdrawing_amount = int(input("How much do you want to withdraw?\n"))
        if withdrawing_amount > balance:
            print("You don't have that much money!")
            print("Deposit more money first, or withdraw a different amount.\n")
        else:
            balance = balance - withdrawing_amount

    elif operation == "3":
        print(balance)

    elif operation == "4":
        exit = True

    else:
        print("Invalid operation, please try again!")

    print("")   # print(\n) would print two empty lines. This prints only 1 empty line (it's just to keep things tidy!)



