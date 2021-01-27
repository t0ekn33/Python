"""Lab 11 - Add New Methods
We need a new method that will provide the balance for any
account. Create that method. Then test it by retrieving the current
balances for both accounts and printing them. Replace the current
code that reaches inside the instance without using a method. This
is not a good coding practice.
Then, create a method for withdrawals. Subtract the withdrawal
amount from the balance. This method should not allow a
withdrawal that would result in a negative balance. As with
deposits, return a code of four for an invalid withdrawal and a zero
for a valid withdrawal. Test with valid and invalid amounts for one
account. Then print the resulting balances for that account.
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

a = BankAccount('Monty Python')  # Create an instance of Bankaccount
b = BankAccount('Guido van Rossum')  # Create another instance
ret_code = a.deposit(100) # Deposit $100 into account 
ret_code = a.deposit(100) # Deposit $100 into account 
if ret_code > 0:   
    print('Deposit failed')  # Return > 0
ret_code = b.deposit(500) # Deposit $500 into account b
if ret_code > 0:   
    print('Deposit failed')  # Return > 0
# print("a.balance", a.balance, "b.balance", b.balance) # This is not good code. We will replace it.

# bal = a.bal()
print("New balance is: $", a.bal(), sep="")

