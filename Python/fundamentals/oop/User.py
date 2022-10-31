class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = Bankaccount(.02, 0)

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:" , self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)
        return self
    
    def enroll(self):
        self.gold_card_points += 200
        if self.is_rewards_member == False:
            self.is_rewards_member = True
        else: 
            print("User is already a member")
        return self
    
    def spend_points(self, amount):
        if self.gold_card_points >= amount: 
            self.gold_card_points -= amount
        else: 
            print("Insufficient points, your current Balance is:", self.gold_card_points)
        return self
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("Balance: $" + str(self.account.balance))
        return self



class Bankaccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else: self.balance -= amount
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


Tyler = User("Tyler", "Toews", "tytoews218@gmail.com", "25")
Tanner = User("Tanner", "Toews", "ttoews18@gmail.com", "25")
Mark = User("Mark", "Richardson", "mrichardson@gmail.com", "33")

Tyler.make_deposit(100).make_withdraw(50).display_user_balance()


Tyler.display_info()
Tyler.enroll()
Tyler.spend_points(50)
Tyler.enroll()

Tanner.display_info()
Tanner.enroll()
Tanner.spend_points(80)

Mark.display_info()
Mark.spend_points(40)



