# bank_account_cli.py

import sys

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance  # Encapsulation with private attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")


def main():
    # Initialize account with example starting balance
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python bank_account_cli.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split command and optional amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
