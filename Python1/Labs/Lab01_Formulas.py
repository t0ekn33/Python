"""
You bought 125 shares of a stock at $25.32 and you sold it at $48.97.
What is the profit?

"""

shares = 125
buy_stock = 25.32
sell_stock = 48.97

ttl_buy = shares * buy_stock
# print('Buy price: ', ttl_buy)

ttl_sell = shares * sell_stock
# print('Sell price: ', ttl_sell)

ttl_diff = ttl_sell - ttl_buy
ttl_diff = '{0:,.2f}'.format(ttl_diff)
print('Profit is $',ttl_diff, sep = '') #using sep


# Profit is $2,956.25

print('####################################')

"""
A product with a price of $127.99 is going on sale.
If the price is reduced by 16%, what will the new price be?
"""

price = 127.99
discount = .84

# print('discount: ', discount)

sale_price = 127.99 * discount
sale_price = '${0:,.2f}'.format(sale_price)  #not using sep
print('Sale price is', sale_price) 

# Sale price is $107.51


