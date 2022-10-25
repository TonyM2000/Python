class BankAccount:
    allusers=[] #For class method
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0
        BankAccount.allusers.append(self) #For class method
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
    def yield_interest(self):
        self.balance = self.balance*(1+self.int_rate)
        return self
    @classmethod
    def all_accounts(cls):
        for user in cls.allusers:
            user.display_account_info()

account1 = BankAccount(.01, 500)
account2 = BankAccount(.03, 10000)
account1.deposit(100).deposit(200).deposit(300).withdraw(250).yield_interest()
account2.deposit(1250).deposit(1250).withdraw(150).withdraw(75).withdraw(420).withdraw(175).yield_interest()
BankAccount.all_accounts()