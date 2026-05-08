pin = 1234
cb = 10000

for i in range(3):
    p = int(input("Enter your pin: "))

    if p == pin:
        print("Correct Pin")
        print("Press 1 : Check Balance")
        print("Press 2 : Send Money")

        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            print("Current Balance is:", cb)

        elif ch == 2:
            wb = int(input("Enter an amount: "))

            if cb >= wb:
                cb = cb - wb
                print("Transaction Successful")
                print("Current Balance is:", cb)

            else:
                print("Insufficient Balance")
                print("Current Balance is:", cb)

        else:
            print("Invalid Choice")

        break

    else:
        print("Wrong Pin")

else:
    print("Card Blocked")