class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0 and not exceed the account balance.")

    def display_balance(self):
        print(f"Account Balance for {self._account_holder_name} (Account #{self._account_number}): ${self._account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create a bank account instance
    account = BankAccount("123456789", "John Doe", 1000)

    # Display the initial balance
    account.display_balance()

    # Deposit some money
    account.deposit(500)

    # Withdraw some money
    account.withdraw(300)

    # Attempt an invalid withdrawal
    account.withdraw(1200)

    # Display the updated balance
    account.display_balance()
