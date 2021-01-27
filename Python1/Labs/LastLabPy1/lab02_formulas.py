
"""lab02_formulas.py

Calculate the profit from the sale of stock and calculate the
new price of a product going on sale.  The results are formatted
without thousands separators using the older method. That is covered
in the alternate completed lab.
"""

shares = 125
purch_price = 25.32
sale_price = 48.97
profit1 = shares * (sale_price-purch_price)
profit2 = shares*sale_price - shares*purch_price   # Another way.
print('Profit is ${0:,.2f} or ${1:,.2f}'.format(
    profit1, profit2))  # Note the continuation technique used here

price = 127.99
discount = 0.16  # or 16%
sale_price = price - price*discount
print('Sale price is ${0:.2f}'.format(sale_price))
