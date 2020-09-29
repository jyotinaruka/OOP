class User:
    def __init__(self, name, balance):
        self.name = name
        self.account_balance = balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


john = User("john", 150)
john.make_deposit(150).make_deposit(5).make_deposit(
    10).make_withdrawal(50).display_user_balance()

mary = User("mary", 100)
mary.make_deposit(70).make_deposit(50).make_withdrawal(
    10).make_withdrawal(30).display_user_balance()

jyoti = User("jyoti", 50)
jyoti.make_deposit(100).make_withdrawal(30).make_withdrawal(
    40).make_withdrawal(10).display_user_balance()

john.transfer_money(jyoti, 100).display_user_balance()
jyoti.display_user_balance()
