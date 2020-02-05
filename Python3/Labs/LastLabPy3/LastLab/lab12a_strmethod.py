"""lab12a_strmethod.py

This class implements the __str__ method to format the account balance
and the account name such that they can be printed.
"""

class BankAccount:  # Top tier class (super class)
    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable
    def deposit(self, amount):     # another method
        if amount < 0:
            return 4   # Negative deposits are really withdrawals
        self.balance += amount
        return 0        # Depost successful
    def withdraw(self, amount):  # a method
        if (self.balance - amount) < 0:
            return 4    # Withdrawal request too large
        self.balance -= amount
        return 0        # Withdrawal successful
    def getbal(self):
        return self.balance
    def __str__(self):
        return 'For account *{0}*, the balance is ${1:,.2f}'.format(
            self.acctname, self.balance)
        

a = BankAccount('Guido van Rossum')  # Create an instance of Bankaccount
b = BankAccount('Monty Python')  # Create another instance
print(a)
print(b)
a.deposit(2500)
print(a)



