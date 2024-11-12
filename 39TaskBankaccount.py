class Bank:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def deposits(self, deposit):
        self.balance += deposit
        return self.balance

    def withdrawel(self, withdraw):
        if withdraw > self.balance:
            print("No sufficient balance")
        elif withdraw>10000:
            print("Withdrawel Limit Exceeded")
        else:
            self.balance -= withdraw
        return self.balance

    def checkDetail(self):
        return self.name, self.age, self.balance

bank = Bank("Asheen", 22, 10000000)
bank.deposits(30000)            
bank.withdrawel(100000)        
print(bank.checkDetail())       
