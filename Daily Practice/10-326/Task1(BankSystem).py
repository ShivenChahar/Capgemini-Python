class Bank :
    def __init__(self, custName, accNO, balance):
        self.custName = custName
        self.accNO = accNO
        self.balance = balance
    
    def withdraw (self, amount) :
        if amount > self.balance :
            print("Insufficient Balance")
        else :
            self.balance = self.balance - amount
            print("The amount Withdrwan is: ", amount)
            print("The remaining amount is: ", self.balance)
    
    def deposit (self, amount) :
        self.balance = self.balance + amount
        print("The amount deposited is: ", amount)
        print("The Current balance is: ",self.balance)
    
    def showBalance (self) :
        print("Current Balance is: ", self.balance) 

ac1 = Bank ("Shiven", 111111, 100000)
ac1.withdraw(500)
ac1.deposit(500)
ac1.showBalance()