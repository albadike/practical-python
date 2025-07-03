class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def __iter__(self):
        # return iter(self.stocks)
        return self.stocks.__iter__()

    # def __next__(self):
    #     if not self.stocks:
    #         raise StopIteration
    #     return self.stocks.pop(0)


portfolio = Portfolio('My Portfolio')
portfolio.add_stock('IBM')
portfolio.add_stock('GOOGL')
portfolio.add_stock('AAPL')

# for-loop: This will automatically call __iter__() and __next__()
# for stock in portfolio:
#     print(stock)

# Manual iteration using iter() and next()
portfolio_iter = iter(portfolio)  # or portfolio.__iter__()
while True:
    try:
        stock = next(portfolio_iter)  # or portfolio_iter.__next__()
        print(stock)
    except StopIteration:
        break
