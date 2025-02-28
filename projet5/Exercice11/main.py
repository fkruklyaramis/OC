class BankAccount:
    def __init__(self, balance: float, account_holder: str):
        self.balance = balance
        self.account_holder = account_holder
    
    def deposit(self,amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

myaccount = BankAccount(1000, "John")
myaccount.display_balance()
myaccount.deposit(500)
myaccount.display_balance()
myaccount.withdraw(200)
myaccount.display_balance()