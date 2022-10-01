class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Your new balance is $", self.balance, "thank you for your deposit.")
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount
            print(f"After your withdraw you have $",self.balance, "remaining, have a nice day.")
        return self
    def display_account_info(self):
        print("Your balance is $",self.balance,"and your interest rate is", self.int_rate)
        return self
    def yield_interest(self):
        self.balance = self.balance*(1+self.int_rate)
        return self

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_balance(self):
        self.account.display_account_info()
        return self

user1= User("Anthony","Anthony@Anthony.com")
user1.make_deposit(500).make_deposit(100).make_withdraw(50)