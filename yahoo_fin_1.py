import yahoo_fin.stock_info as si

apple = si.get_live_price('aapl')
amazon = si.get_live_price('AMZN')
nvidia = si.get_live_price('NVDA')

# get the stock info using Python

print("The stock price of Apple: ",apple)
print ("The stock price of Amazon: ",amazon)
print("The stock price of Nvidia: ",nvidia)