from nsetools import Nse
import time

nse = Nse()

stocks = ['INFY', 'ABB', 'MINDTREE', 'BHEL']

while True:
    for stock in stocks:
        data = nse.get_quote(stock)
        print(f"{stock:>8}, {data['lastPrice']:>10}, {data['dayHigh']:>10}, {data['pChange']:>10}")
        time.sleep(1)