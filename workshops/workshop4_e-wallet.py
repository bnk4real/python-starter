# Sample E-Wallet model

def initFunc():
    print("Welcome to E-Wallet, what would you like to do?")
    print("Prees T to Topup :")
    print("Press P to Pay :")
    print("Press C to Check Balance :")

    init = input("Enter : ")

    wallet = 0

    if init == "T":
    # business logic
        topup = float(input("Enter topup amount : "))
        if topup == 0:
            print("Enter at least 1 value")
        while topup != 0:
            sum = 0
            wallet = topup + wallet
            sum += wallet
            print("Wallet amount : ", sum)
            topup = float(input("Enter topup amount : "))
        else:
            initFunc()
            
    elif init == "P":
    # business logic
        topup = float(input("Enter Pay amount : "))
        if topup == 0:
            print("Enter at least a value")
        while topup != 0:
            # wallet = topup - sum
            wallet = topup - wallet
            print("Wallet amount : ", wallet)
            topup = float(input("Enter topup amount : "))
        else:
            initFunc()
    elif init == "C":
        print(wallet)

# Start
initFunc()