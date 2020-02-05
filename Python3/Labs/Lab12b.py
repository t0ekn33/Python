"""Lab 12b - Comparisons
When you compare for equality, the default version of __eq__ is called
automatically and it will blindly compare two instances which will never be equal.
To override this result, implement one or more of the newer magic methods – in
our case __eq__. Use this magic method to compare the balances of the two
accounts. Test by using equal and non-equal balances
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
    # def __str__(self):
    #         return 'For account *{0}*, the balance is ${1:,.2f}'.format(self.acctname, self.balance)
    def __eq__(self,other):
        print(self.balance, other.balance)
        if self.balance == other.balance:
            return True
        else:
            return False

a = BankAccount('Monty Python')  # Create an instance of Bankaccount
b = BankAccount('Guido van Rossum')  # Create another instance

a.deposit(500)
b.deposit(2500)

if a == b:
    print("Same")
else:
    print("Different")
    
a.deposit(2000)
b.deposit(0)

if a == b:
    print("Same")
else:
    print("Different")
    