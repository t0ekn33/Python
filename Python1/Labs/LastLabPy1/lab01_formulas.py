"""lab01_formulas.py

Calculate the profit from the sale of stock and calculate the
new price of a product going on sale. Note how some math operators
are separated by spaces and others aren't.  The reason can be found
in PEP8 under Whitespace in Expressions and Statements.
"""

shares = 125
purch_price = 25.32
sale_price = 48.97
profit1 = shares * (sale_price-purch_price)
profit2 = shares*sale_price - shares*purch_price   # Another way.
print('Profit is', profit1, profit2)  # Is there a difference?

price = 127.99
discount = 0.16  # or 16%
sale_price = price - price*discount  # Parentheses required here?
print('Sale price is', sale_price)  # unformatted
