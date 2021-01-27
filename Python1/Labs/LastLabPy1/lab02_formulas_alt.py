
"""lab02_formulas_alt.py

Calculate the profit from the sale of stock and calculate the
new price of a product going on sale.  With the older method of
formatting, you must use the format function to include thousands
separators.  It is very awkward.  The newest method (f-strings) is
much clearer, but you must have Python version 3.6 or higher to use it
"""

shares = 125
purch_price = 25.32
sale_price = 48.97
profit1 = shares * (sale_price-purch_price)
profit2 = shares*sale_price - shares*purch_price
print(f'Profit is ${profit1:,.2f} or ${profit2:,.2f}')  # Newest method
print('Profit is $%s or $%s' % (
    format(profit1, ',.2f'), format(profit2, ',.2f')))  # Older method

price = 127.99
discount = 0.16  # or 16%
sale_price = price - price*discount
print(f'Sale price is ${sale_price:.2f}')
print('Sale price is $%.2f' % (sale_price))
