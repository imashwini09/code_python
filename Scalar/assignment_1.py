class BankAccount:
    def __init__(self,accountNumber,balance,roi):
        self.accountNumber = accountNumber
        self.balance = balance
        self.roi = roi

    def getSimpleInterest(self,time):
        self.simple_interest = (self.balance * time * self.roi)/100
        return self.simple_interest

    def getBalanceWithInterest(self,time):
        self.BalanceWithInterest = self.getSimpleInterest(time) + self.balance
        return self.BalanceWithInterest

b = BankAccount(123,50000,10)
print(b.getSimpleInterest(5))
print(b.getBalanceWithInterest(5))