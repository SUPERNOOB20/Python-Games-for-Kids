balance = 100
exit    = False

while exit == False:
    operation = input("Choose an operation:\n  1) Deposit  2) Withdraw  3) Exit\n")

    if operation == "1":
        balance = balance + int(input("How much do you want to deposit?"))

    elif operation == "2":
        balance = balance - int(input("How much do you want to withdraw?"))

    elif operation == "3":
        exit = True

    else:
        print("Invalid operation, please try again!")