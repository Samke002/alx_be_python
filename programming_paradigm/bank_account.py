# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default = 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Return True if successful, False otherwise."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
