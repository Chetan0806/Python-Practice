def show_menu():
    """Displays the main ATM menu choices."""
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def check_balance(balance):
    """Displays the current balance."""
    print(f"Your current balance is: ${balance:.2f}")


def deposit(balance):
    """Asks for a deposit amount, adds it to the balance, and returns the new balance."""
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} successfully deposited.")
    else:
        print("Invalid deposit amount.")
    return balance


def withdraw(balance):
    """Asks for a withdrawal amount, validates it against the current balance,

    and returns the updated balance.
    """
    amount = float(input("Enter amount to withdraw: $"))
    if amount > balance:
        print("Transaction Declined: Insufficient funds!")
    elif amount <= 0:
        print("Invalid withdrawal amount.")
    else:
        balance -= amount
        print(f"${amount:.2f} successfully withdrawn.")
    return balance

def main():
    current_balance = 1000.0

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance(current_balance)

        elif choice == "2":
            current_balance = deposit(current_balance)

        elif choice == "3":
            current_balance = withdraw(current_balance)

        elif choice == "4":
            print("\nThank you for using our ATM. Take Care!")
            break

        else:
            print("Invalid choice. Please select an option between 1 and 4.")


main()