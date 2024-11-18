#Creating a class BankAccount
bank_name ="Tech4Girls Bank"

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder= account_holder
        self.balance=  0

#Defining a method deposit(amount) to add money to the account.
    def deposit(self, amount): 
        if amount > 0: 
            self.balance += amount 
            print(f"You deposited {amount}. New balance is {self.balance}.") 
        else: print("Invalid deposit amount.")

#Defining a method withdraw(amount) to deduct money.
    def withdraw(self, amount): 
        if 0 < amount <= self.balance: 
            self.balance -= amount 
            print(f"You withdrew {amount}. New balance is {self.balance}.") 
        elif amount > self.balance: 
            print("Insufficient funds.") 
        else: 
            print("Invalid withdrawal amount.")

#Defining a static method bank_policy() that prints a generic policy message.
    @staticmethod
    def bank_policy(): 
        print("Bank Policy: Your account will be closed if there are no transactions made for about 2 years.")

#Defining a  class method get_bank_name() to return the bank name.
    @classmethod
    def get_bank_name(pv): 
        return pv.get_bank_name
    
#Creating instances of the BankAccount class 
accounta = BankAccount("Precious") 

print()
#Testing deposit method 
accounta.deposit(5000) 
 
print()
#Testing withdraw method 
accounta.withdraw(900) 

print()
#Testing static method for bank policy
BankAccount.bank_policy()
print()
#Testing class method 
print("Bank Name:", BankAccount.get_bank_name())
print()
# Displaying account details 
print(f"Account Holder: {accounta.account_holder}, Balance: {accounta.balance}") 
