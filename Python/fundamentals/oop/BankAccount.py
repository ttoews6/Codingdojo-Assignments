class Bankaccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        # print("Balance:", self.balance)
        return self
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else: self.balance -= amount
        # print("Balance:", self.balance)
        return self
    def display_account_info(self):
        print("Balance: $"+ str(self.balance))
        return self
    def yield_interest(self):
        int_rate = 0
        if self.balance > 0:
            int_rate = self.balance * self.int_rate
            self.balance += int_rate
        else: print("Current balance is negative")
        return self

account1 = Bankaccount(.05, 15)
account2 = Bankaccount(.07, 50)

account1.deposit(100).deposit(25).deposit(33).withdraw(40).yield_interest().display_account_info()
account2.deposit(75).deposit(75).withdraw(20).withdraw(10).withdraw(45).withdraw(10).yield_interest().display_account_info()