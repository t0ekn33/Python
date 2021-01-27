""" Lab11 - Add two new methods

This program adds two methods to the original code.  One method simply
returns the current balance of the account.  The other method allows
a withdrawal in any amount as long as there is money in the account
to cover it.  A valid withdrawal results in a zero return.  An
excessive withdrawal is denied with a return of 4.
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
        return 0        # Withdrwal successful
    def getbal(self):
        return self.balance

a = BankAccount('Guido van Rossum')  # Create an instance of Bankaccount
b = BankAccount('Monty Python')  # Create another instance
a.deposit(100)   # Deposit $100 into account represented by variable a
b.deposit(500)  # Deposit $500 into account represented by variable b
return_code = a.withdraw(150)  # Excessive withdrawal
if return_code > 0:
    print('Invalid withdrawal')
return_code = a.withdraw(45.87)
if return_code > 0:
    print('Invalid withdrawal')
print('New account balance is $', a.getbal(), sep = '')


