# ---------------:: BankAccount Class ::---------------- #
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

# ---------------:: User Class ::--------------------- #


class User:
    def __init__(self, name, balance):
        self.name = name
        self.account = {
            "saving": BankAccount(0.02, balance),
            "checking": BankAccount(0.01, balance)
        }

    def make_deposit(self, account_type, amount):
        self.account[account_type].deposit(amount)

    def make_withdrawal(self, account_type, amount):
        self.account[account_type].withdraw(amount)

    def display_user_balance(self):
        print(f"User: {self.name}")
        print(f"    Savings balance: {self.name}")
        self.account["saving"].display_account_info()
        print(f"    Checking balance: {self.name}")
        self.account["checking"].display_account_info()

    def transfer_money(self, other_user, amount):
        self.make_withdrawal("checking", amount)
        other_user.make_deposit("checking", amount)


# -------------:: Use User & BankAccount Class ::------------- #

john = User("john", 150)
john.make_deposit("saving", 150)
john.make_deposit("saving", 5)
john.make_deposit("saving", 10)
john.make_withdrawal("checking", 50)
john.display_user_balance()

mary = User("mary", 100)
mary.make_deposit("saving", 70)
mary.make_deposit("saving", 50)
mary.make_withdrawal("checking", 10)
mary.make_withdrawal("checking", 30)
mary.display_user_balance()
