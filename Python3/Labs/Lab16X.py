"""Lab 16
Change the previous program to prevent a minimum balance
account from being created without an initial deposit that meets the
required minimum. Capture the error in the main program and print
an appropriate message indicating the problem. The message
should contain a description of the problem, the attempted deposit
amount and the minimum requirement.
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

class DepMinAcct(BankAccount):
    pass
def DepositError(amt):    
    if amt < 1000:
        ex = DepositError('Deposit too small', amt, 1000)
        raise ex  # The instance ex is passed to except on a
    else:         # DepositError
        print('Deposit OK')
    return
        


try:
    DepositError(100)
except DepositError as err1:
    print(type(err1.args), len(err1.args), err1)  # err1 is actually a tuple
    print(err1.args[0], '-', err1.args[1], '  Need at least', err1.args[2])
    print(*err1.args) # Do you remember what the * does in a function call? Unpacks the tuple and passes them 1 by 1

# a = BankAccount('Guido van Rossum')  # Create an instance of Bankaccount
# b = BankAccount('Monty Python')  # Create another instance
# # print('Number of accounts -', BankAccount.acct_cntr)  # print class variable
# # del a
# # print('Number of accounts -', BankAccount.acct_cntr)
# c = MinBalAcct('Eric Idle', 5000,1000)  # Create a minimum balance instance
# print('Number of accounts -', BankAccount.acct_cntr)
# print(c)
# if c.withdraw(4500) > 0:
#     print('Invalid withdrawal')
# if c.withdraw(3500) > 0:
#     print('Invalid withdrawal')
# print(c)
# # del c
# # print('Number of accounts -', BankAccount.acct_cntr)