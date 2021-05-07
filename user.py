class User():
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

jayden = User("Jayden Python", "jayden@gmail.com")
nick = User("Nick Css", "nick@gmail.com")
dojo = User("Dojo Html", "dojo@gmail.com")

jayden.make_deposit(500)
jayden.make_deposit(200)
jayden.make_deposit(100)
jayden.make_withdrawal(400)
jayden.display_user_balance()

nick.make_deposit(600)
nick.make_deposit(300)
nick.make_withdrawal(100)
nick.make_withdrawal(300)
nick.display_user_balance()

dojo.make_deposit(800)
dojo.make_withdrawal(300)
dojo.make_withdrawal(50)
dojo.make_withdrawal(200)
dojo.display_user_balance()