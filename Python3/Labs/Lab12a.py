"""Lab 12a - Stringify
Add a method to your code to override the default __str__ hidden
method. This method requires that the object returned must be a
string. The new method should return, in printable form, the name
associated with the account as well as the balance.
"""

class BankAccount:  # Top tier class (super class) in Python 2 or 3
# class BankAccount:  # works fine in Python 3.  Parens not require

    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable
    def deposit(self, amount): # another method
        if amount < 0:
            return 4   # Negative deposits are really withdrawals
        self.balance += amount
        return 0        # Depost successful
    def bal(self):     # method that gets balance
            return self.balance
    def __str__(self):
            return 'For account *{0}*, the balance is ${1:,.2f}'.format(self.acctname, self.balance)


a = BankAccount('Monty Python')  # Create an instance of Bankaccount
b = BankAccount('Guido van Rossum')  # Create another instance

print(a)
print(b)
a.deposit(2500)
print(a)