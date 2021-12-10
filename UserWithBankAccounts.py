class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(account_name='', int_rate=0.004, balance=0)
    
    def make_deposit(self, amount, account_name):
        self.account.deposit(amount, account_name)
        return self

    def make_withdrawal(self, amount, account_name):
        self.account.withdraw(amount, account_name)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, account_name, int_rate=0.004, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance
        
    def deposit(self, amount, account_name):
        self.account_balance += amount
        return self

    def withdraw(self, amount, account_name):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Current {self.account_name} Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance += (self.account_balance * self.int_rate)
        return self

#create instances of class User
tom = User("Tom", "tom@cruise.com")
ethan = User("Ethan", "ethan@hunt.com")

#create instances of class BankAccount
checking = BankAccount('Checking',1000)
savings = BankAccount('Savings',2000)

tom.make_deposit(200,checking).make_deposit(300,checking).make_deposit(500,savings).make_withdrawal(200,checking).account.yield_interest()
tom.display_user_balance()
ethan.make_deposit(300,checking).make_deposit(500,savings).make_deposit(500,savings).make_withdrawal(150,checking).account.yield_interest()
ethan.display_user_balance()
