# stock.py
#
# Exercise 4.1

import fileparse
import pprint


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        # self.cost     # Its nice that Python allows us to use 'cost' 
                        # instead of the expected '_cost' for the rest of our code
                        # or even without it at all
    
    @property
    def cost(self):
        self._cost = self.shares * self.price
        return self._cost

    def sell(self, sold_shares):
        if sold_shares > self.shares:
            raise ValueError("Not enough shares to sell")
        self.shares -= sold_shares
        return self.shares


def main():
    # Example usage of the Stock class
    # stock = Stock("AAPL", 100, 150.0)
    # print(f"Cost of {stock.name}: ${stock.cost()}")
    # sold = 55
    # try:
    #     stock.sell(sold)
    # except ValueError as e:
    #     print(e)
    # print(f"Shares left after selling {sold} units: {stock.shares}")

    # Example usage of fileparse to read a CSV file and create Stock objects
    filename = 'Data/portfolio.csv'
    # Select columns by index; or by name if has_header=True
    select = ['name', 'shares', 'price']
    types = [str, int, float]
    has_header = True                      # Set to False if the file has no header row
    silence_errors = True                  # Set to False to see error messages

    with open(filename, 'rt') as file:
        try:
            record_list_of_dicts = fileparse.parse_csv(file, select=select, types=types, has_header=has_header)
        except TypeError as e:
            if not silence_errors:
                print(f"**Error: File not found or mismatched 'select' columns {e}**")
            # Stop the program immediately
            raise   # 1 is conventional for error; 0 for clean exit

    # portfolio_list_of_objects = [Stock(record['name'], record['shares'],record['price']) for record in record_list_of_dicts]
    portfolio_list_of_objects = [Stock(**record_dict) for record_dict in record_list_of_dicts]

    for portfolio in portfolio_list_of_objects:
        print(f"Stock: {portfolio.name}, Shares: {portfolio.shares}, Price: ${portfolio.price:.2f}, Cost: ${portfolio.cost:.2f}")

    sum_all_portfolio_objects = sum([portfolio.cost for portfolio in portfolio_list_of_objects])
    print(f"\nTotal portfolio cost: ${sum_all_portfolio_objects:.2f}")


if __name__ == "__main__":
    main()
