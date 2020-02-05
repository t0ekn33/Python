"""lab18b_imp.py

This program imports only the module.  This requires every class
reference to be accessed through dot notation.  This includes all
references to class variables.

"""

import sys
#sys.path.append('/home/student/imports') # temporary addition to path
sys.path.append('c:/pyprogs/imports') # temporary addition to path
import banker

a = banker.BankAccount('Guido van Rossum')  # Create an instance of Bankaccount
b = banker.BankAccount('Monty Python')  # Create another instance
print('Number of accounts -', banker.BankAccount.acct_cntr)  # print class variable
del a
print('Number of accounts -', banker.BankAccount.acct_cntr)
c = banker.MinBalAcct('Eric Idle', 5000,1000)  # Create a minimum balance instance
print('Number of accounts -', banker.BankAccount.acct_cntr)
print(c)
c.withdraw(4500)
try:
    d = banker.MinBalAcct('John Cleese', 500,1000)
except ValueError as msg:
    print("Account not established -", msg)
print(c)



