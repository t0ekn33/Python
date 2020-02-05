"""Lab 14
• Add the following statements to the end of your program
del a
print('Number of accounts -', BankAccount.acct_cntr)
• What is the problem and what has to change?
• Implement the magic method needed to get the correct result. if
necessary, go back a few slides to the list of these methods.
• If you use an older version of Python and execute from command
line, you may get an error message after the program has run
successfully. We will discuss.
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
        BankAccount.acct_cntr -= 1  # Incrememnt the account counter

a = BankAccount('Guido van Rossum')  # Create an instance of Bankaccount 
print('Number of accounts +', BankAccount.acct_cntr)  
b = BankAccount('Monty Python')  # Create another instance 
print('Number of accounts +', BankAccount.acct_cntr)  # print class variable

del a
print('Number of accounts -', BankAccount.acct_cntr)

del b
print('Number of accounts -', BankAccount.acct_cntr)