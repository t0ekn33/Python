""" Keyboard Input

The input() function will get data from the keyboard
"""

name = input('Please enter your name: ')
age= input('Please enter your age in years: ')
# The age entered must be converted before being used in calculations.
age_in_years = int(age)
print(name, 'has been eligible to drive an automobile for',
      age_in_years - 16, 'years') # Note the continuation method used


