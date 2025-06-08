# 2_report.py
#
# Exercise 2.4

import collections
import csv
import pprint
import sys


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

        # Hardcoded; One advantage is the ability to convert types readily
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

        # Check if portfolio_name exists in prices
        for price_dict in prices:
            if portfolio_name in price_dict.values():
                price_diff = price_dict['price'] - portfolio_price
                report_list.append(
                    (portfolio_name, portfolio_shares, price_dict['price'], price_diff))
    return report_list


def print_report(report_list):
    """ Print Report """
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # separator = '----------'
    # print("\n%10s %10s %-10s %10s" % headers)
    # print("%10s %10s %10s %10s" % (separator, separator, separator, separator))

    # for report in report_list:
    #     # unpack report tuple containing (name, shares, price, price_diff)
    #     print("%10s %10d $%-9.2f %10.2f" % report)

    # Tabulate report
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '----------'
    print("\n%10s %10s %-10s %10s" % headers)
    print("%10s %10s %10s %10s" % (separator, separator, separator, separator))

    # Using C-style formatting
    # Right-justified by default
    # Use - to left-justify
    for report in report_list:
        # unpack report tuple containing (name, shares, price, price_diff)
        print("%10s %10d $%-9.2f %10.2f" % report)

    # # Or Using f-string for better readability
    # for name, shares, price, price_diff in report_list:
    #     print(f"{name:10} {shares:10} ${price:10.2f} {price_diff:10.2f}")

    # Counting and totalling shares: collections.Counter()
    counter_dict = collections.Counter()
    for report in report_list:
        counter_dict[report[0]] += report[1]

    # Reprint
    print("\n%10s %10s" % (headers[0], headers[1]))
    print("%10s %10s" % (separator, separator))
    for name, shares in counter_dict.items():
        print(f"{name:>10} {shares:>10}")

    # Rank the totals
    print(f'\n{counter_dict.most_common(3)=}')
    return None


def portfolio_report(portfolio_filename,price_filename):
    """Main function to read data and generate report."""
  
    print(f"Reading prices from {price_filename} and portfolio from {portfolio_filename}...")
    
    price_list_of_dicts = read_prices(price_filename)
    portfolio_list_of_dicts = read_portfolio(portfolio_filename)
    print(f'{portfolio_list_of_dicts=}')

    if price_list_of_dicts and portfolio_list_of_dicts:
        report_list_of_tuples = make_report(
            portfolio_list_of_dicts, price_list_of_dicts)
        print(f'{report_list_of_tuples=}')
        if report_list_of_tuples:
            print_report(report_list_of_tuples)
        else:
            print("No matching data found in the report.")
    else:
        print("No data available to generate report.")
    return None


def main():
    # This segments shows up when running the script in the CLI using:
    # python3 2_report.py Data/portfolio.csv Data/prices.csv OR
    # python3 2_report.py "Data/portfolio.csv" "Data/prices.csv"
    
    # But not when imported as a module, using:
    # from report import portfolio_report
    # portfolio_report("Data/portfolio.csv", "Data/prices.csv")
    # NOTE: Running in REPL rejects 2_report.py as a module name, so use report.py
   
    # Check if the correct number of arguments are provided
    # sys.argv[0] is the script name, so we expect at least 3 arguments
    if len(sys.argv) < 3:
        print("Usage: python3 2_report.py <portfolio_file> <prices_file>")
        sys.exit(1)
        
    # Call the function with command line arguments
    portfolio_report(*sys.argv[1:])     # OR portfolio_report(sys.argv[1], sys.argv[2])
    
    # Confirm args numbering
    [print(i, arg) for i,arg in enumerate(sys.argv)]
    # Output:
    # 0 2_report.py
    # 1 Data/portfolio.csv
    # 2 Data/prices.csv
    
    return None
    
if __name__ == "__main__":
    main()