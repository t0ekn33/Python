"""Lab 15
• Change the previous program to allow, in addition to the normal
account, an account with a minimum balance. Do this through a
new class that inherits from the original. Make sure the new class
does the following:
• Provides for an initial deposit and a specified minimum balance as
well as a name on account creation. For now, don't check to see that
the initial deposit meets the minimum requirement.
• Does not permit a withdrawal that takes the balance below the
minimum. Return zero for valid withdrawals. Otherwise return 4.
• When an instance is printed, print the balance and the minimum
required for minimum-balance accounts.
• Confirm that the original methods work for the new class.
• Note – class variables are referenced through the original class
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
class BankAccount2(BankAccount):
    acct_cntr = 0         # class variable
    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable
        self.minbal = 5
        BankAccount.acct_cntr += 1  # Incrememnt the account counter
    def deposit(self, amount):     # another method
        if amount < 0:  
            return 4   # Negative deposits are really withdrawals
        self.balance += amount
        return 0        # Depost successful
    def withdraw(self, amount):  # a method
        if (self.balance - amount) <= 5:
            return 4    # Withdrawal request too large
        self.balance -= amount
        return 0        # Withdrwal successfu
    def __str__(self):
        return 'Account Name: *{0}*, Balance: ${1:,.2f}, Min Balance: ${2:,.2f}'.format(
            self.acctname, self.balance, self.minbal)



a = BankAccount2('Guido van Rossum')  # Create an instance of Bankaccount 
a.deposit(200)
ret_code = a.withdraw(600) # Deposit $500 into account b
if ret_code > 0:   
    print('Withdraw failed for', a)  # Return > 0
else:
    print(a)

b = BankAccount2('George Bush')  # Create an instance of Bankaccount 
ret_code = b.deposit(200) # Deposit $500 into account b
if ret_code > 0:   
    print('Deposit failed for', b)  # Return > 0
else:
    print(b)