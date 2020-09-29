class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"BankAccount balance: ${self.balance}")
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate / 30
        interest = round(interest)
        self.deposit(interest)
        return self


david = BankAccount(0.02, 200)
david.deposit(100).deposit(100).deposit(100).withdraw(
    100).yield_interest().display_account_info()


dave = BankAccount(0.04, 500)
dave.deposit(50).deposit(50).withdraw(
    50).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()
