#
#   Create a simple banking system that allows user to deposit, withdraw and check balance. 
#
balance = 0

def deposit():
    global balance
    try:
        deposit = float(input("Enter deposit amount: "))
        balance += deposit
        print(f"${deposit:.2f} deposited. Balance: ${balance:.2f}")
        print("-"*19)
    except ValueError:
        print("Incorrect value. Please enter numeric amount.")

def withdraw():
    global balance
    try:
        withdraw = float(input("Enter withdrawl amount: "))
        if withdraw > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw
            print(f"${withdraw:.2f} withdrawn. Balance: ${balance:.2f}")
            print("-"*19)
    except ValueError:
        print("Incorrect value. Please enter numeric amount.")

while True:
    try:
        print("Simple Personal Bank")
        print("-"*19)
        print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        opt = int(input("Choose option: "))
    except ValueError:
        print("invalid option. Please try again.")
    print("-"*19)

    if opt == 1:
        deposit()
    elif opt == 2:
        withdraw()
    elif opt == 3:
        print(f"Current balance: ${balance:.2f}")
        print("-"*19)
    elif opt == 4:
        break
    else:
        ("Incorrect option. Please select valid option.")