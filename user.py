class User:
    def __init__(self, name, balance):
        self.name = name
        self.account_balance = balance

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


john = User("john", 150)
john.make_deposit(150)
john.make_deposit(5)
john.make_deposit(10)
john.make_withdrawal(50)
john.display_user_balance()

mary = User("mary", 100)
mary.make_deposit(70)
mary.make_deposit(50)
mary.make_withdrawal(10)
mary.make_withdrawal(30)
mary.display_user_balance()

jyoti = User("jyoti", 50)
jyoti.make_deposit(100)
jyoti.make_withdrawal(30)
jyoti.make_withdrawal(40)
jyoti.make_withdrawal(10)
jyoti.display_user_balance()

john.transfer_money(jyoti, 100)
john.display_user_balance()
jyoti.display_user_balance()
