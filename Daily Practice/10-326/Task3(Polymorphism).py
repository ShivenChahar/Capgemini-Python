class CreditCard:
     def pay(self,amount):
          print("the amount paid through credit card is:",amount)
class UPI:
     def pay(self,amount):
          print("the amount paid through UPI is:",amount)
class Cash:
     def pay(self,amount):
          print("the amount paid through cash is :",amount)
      
var=[CreditCard(),UPI(),Cash()]
amt=int(input("enter an amount to pay:"))
for i in var:
     i.pay(amt)