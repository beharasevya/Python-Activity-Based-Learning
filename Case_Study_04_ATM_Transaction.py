print("ATM TRANSACTION")
balance = 5000.0

while True:
    print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Available balance: ₹{balance:.2f}")
    elif choice == "2":
        amount = float(input("Deposit amount: ₹"))
        if amount > 0:
            balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")
    elif choice == "3":
        amount = float(input("Withdrawal amount: ₹"))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful.")
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice.")
