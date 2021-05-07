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

jayden.make_deposit(500).make_withdrawal(200).display_user_balance()
nick.make_deposit(600).make_withdrawal(100).display_user_balance()
dojo.make_deposit(700).make_withdrawal(300).display_user_balance()