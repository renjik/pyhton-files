class Bank_Account:
    def __init__(self,balance):
        self.num=int(input("enter the number"))
        self.name= input("enter the name:")
        self.balance= balance
 

    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
# l=()
# print("1.create account\n2.deposit\n3.withdraw\n4.show balance\n5.Exit")
# while True:
#     n=int(input("Enter the choice:"))
#     if n==1:
#         x=bank(1,"name",100)
#         1.append(x)

 
obj = Bank_Account()
  
# Calling functions with that class object
obj.deposit()
obj.withdraw()
obj.display()