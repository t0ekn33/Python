"""lab16_raise.py

This program includes a subclass (MinBalAcct) that inherits from
BankAccount and then overrides __init__, __str__ and withdraw.
It prevents accounts being set up that don't meet the minimum
balance requirements by raising a ValueError.
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
        if minbal > deposit:
            raise ValueError('Deposit too small', deposit, minbal)        
        self.minimum_bal = minbal
        self.balance = deposit
        BankAccount.acct_cntr += 1
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_bal:
            return 4
        self.balance -= amount
        return 0
    def __str__(self):
        return ("The balance for this account is ${0:,.2f}\n" +
               "The minimum balance is ${1:,.0f}").format(
                self.balance, self.minimum_bal)    
        
a = BankAccount('Guido van Rossum')  # Create an instance of Bankaccount
b = BankAccount('Monty Python')  # Create another instance
print('Number of accounts -', BankAccount.acct_cntr)  # print class variable
del a
print('Number of accounts -', BankAccount.acct_cntr)
c = MinBalAcct('Eric Idle', 5000,1000)  # Create a minimum balance instance
print('Number of accounts -', BankAccount.acct_cntr)
print(c)
if c.withdraw(4500):
    print('Invalid withdrawal request')
print(c)
try:
    d = MinBalAcct('John Cleese', 500,1000)
except ValueError as msg:
    print(type(msg.args))
    print("Account not established - ", msg.args[0], '.\n$',
          msg.args[1], ' does not meet the minimum requirement of $',
          msg.args[2], sep = '')

if 'd' in globals():
    print('Variable "d" was established')
else:   # Verifies the instantiation did not occur.
    print('Variable "d" was not created')
    




