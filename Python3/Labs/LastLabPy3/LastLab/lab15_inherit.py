
"""lab15_inherit.py

This program includes a subclass (MinBalAcct) that inherits from
BankAccount and then overrides __init__, __str__ and withdraw.
Note - class variables are referenced through the original class.
"""

class BankAccount:  # Top tier class (super class)
    acct_cntr = 0         # class variable
    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable
        BankAccount.acct_cntr += 1  # Incrememnt the account counter
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
    def __str__(self):
        return 'For account *{0}*, the balance is ${1:,.2f}'.format(
            self.acctname, self.balance)
    def __eq__(self, other):
        print('__eq__ method entered', self.balance, other.balance) 
        if self.balance == other.balance:
            return True
        return False
    def __del__(self):
        BankAccount.acct_cntr -= 1 

class MinBalAcct(BankAccount):
    def __init__(self, name, deposit, minbal):
        self.minimum_bal = minbal
        self.balance = deposit
        self.acctname = name
        BankAccount.acct_cntr += 1
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_bal:
            return 4
        else:
            self.balance -= amount
            return 0
    def __str__(self):
        # Note the technique for creating/continuing the returned string.
        return ("The balance for *{0}* account is ${1:,.2f}\n" +
               "The minimum balance is ${2:,.0f}"
                ).format(self.acctname, self.balance, self.minimum_bal)    
        
a = BankAccount('Guido van Rossum')  # Create an instance of Bankaccount
b = BankAccount('Monty Python')  # Create another instance
print('Number of accounts -', BankAccount.acct_cntr)  # print class variable
del a
print('Number of accounts -', BankAccount.acct_cntr)
c = MinBalAcct('Eric Idle', 5000,1000)  # Create a minimum balance instance
print('Number of accounts -', BankAccount.acct_cntr)
print(c)
if c.withdraw(4500) > 0:
    print('Invalid withdrawal')
if c.withdraw(3500) > 0:
    print('Invalid withdrawal')
print(c)
del c
print('Number of accounts -', BankAccount.acct_cntr)


