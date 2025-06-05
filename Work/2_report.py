# 2_report.py
#
# Exercise 2.4

import csv
import pprint


def read_prices(filename):
    """Read a Price CSV File"""

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        name_price_list = []

        # Hardcoded: can be improved using zip()
        for row in reader:
            if row:
                row_dict = {
                    'name': row[0],
                    'price': float(row[1])
                }
                name_price_list.append(row_dict)
        return name_price_list


# price_list_of_dicts = read_prices("Data/prices.csv")
# pprint.pprint(price_list_of_dicts)


def read_portfolio(filename):
    """Read a Portfolio CSV file"""

    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        portfolio_list = []
        
        # hardcoded
        # for row in rows:
        #     row_dict = {
        #         'name': row[0],
        #         'shares': int(row[1]),
        #         'price': float(row[2])
        #     }
        #     portfolio_list.append(row_dict)
            
        for row in rows:
            row_dict = dict(zip(headers, row))
            portfolio_list.append(row_dict)
    return portfolio_list


# portfolio_list_of_dicts = read_portfolio("Data/portfolio.csv")
# print(portfolio_list_of_dicts)


def make_report(portfolios, prices):
    """ Make Report """

    report_list = []

    for portfolio_dict in portfolios:
        portfolio_name = portfolio_dict['name']
        portfolio_shares = int(portfolio_dict['shares'])
        portfolio_price = float(portfolio_dict['price'])

        for price_dict in prices:
            if portfolio_name in price_dict.values():
                price_diff = price_dict['price'] - portfolio_price
                report_list.append(
                    (portfolio_name, portfolio_shares, price_dict['price'], price_diff))

    return report_list


# main()
price_list_of_dicts = read_prices("Work/Data/prices.csv")
portfolio_list_of_dicts = read_portfolio("Work/Data/portfolio.csv")
print(f'{portfolio_list_of_dicts=}')

if price_list_of_dicts and portfolio_list_of_dicts:
    reports = make_report(portfolio_list_of_dicts, price_list_of_dicts)

    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '----------'
    print("%10s %10s %-10s %10s" % headers)
    print("%10s %10s %10s %10s" % (separator, separator, separator, separator))

    # Using C-style formatting
    # Right-justified by default
    # Use - to left-justify
    for report in reports:
        # unpack report tuple containing (name, shares, price, price_diff)
        print("%10s %10d $%-9.2f %10.2f" % report)

    # # Or Using f-string for better readability
    # for name, shares, price, price_diff in reports:
    #     print(f"{name:10} {shares:10} ${price:10.2f} {price_diff:10.2f}")
else:
    print("No data available to generate report.")