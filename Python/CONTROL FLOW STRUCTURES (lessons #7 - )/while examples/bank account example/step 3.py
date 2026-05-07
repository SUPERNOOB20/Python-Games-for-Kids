balance = 100
exit    = False

while exit == False:
    operation = input("Choose an operation:\n  1) Deposit  2) Withdraw  3) Exit\n")

    if operation == "1":
        balance = balance + input("How much do you want to deposit?")

    elif operation == "2":
        withdrawing_amount = int(input("How much do you want to withdraw?"))
        if withdrawing_amount < balance:
            print("You don't have that much money!")
            print("Deposit more money first, or withdraw a different amount")
        else:
            balance = balance - withdrawing_amount

    elif operation == "3":
        exit = True

    else:
        print("Invalid operation, please try again!")