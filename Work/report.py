# report.py 
#
# Exercise 2.4

import collections
import csv
import pprint
import sys
import tableformat as tf
from portfolio import Portfolio
import fileparse
import stock


def read_prices(filename):
    """Read a Price CSV File"""

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        price_list_of_dicts = []

        # Hardcoded: can be improved using zip()
        for row in reader:
            if row:
                row_dict = {
                    'name': row[0],
                    'price': float(row[1])
                }
                price_list_of_dicts.append(row_dict)
        return price_list_of_dicts


def read_portfolio(filename):
    """Read a Portfolio CSV file"""
    ## Alternatively
    # with open(filename) as file:
    #     rows = csv.reader(file)
    #     headers = next(rows)
    #     portfolio_list_of_dicts = []

    #     ## Hardcoded; One advantage is the ability to convert types readily
    #     # for row in rows:
    #     #     row_dict = {
    #     #         'name': row[0],
    #     #         'shares': int(row[1]),
    #     #         'price': float(row[2])
    #     #     }
    #     #     portfolio_list.append(row_dict)

    #     for row in rows:
    #         row_dict = dict(zip(headers, row))
    #         portfolio_list_of_dicts.append(row_dict)
    # return portfolio_list_of_dicts
    
    ## Alternative: using fileparse.parse_csv()
    with open(filename, 'rt') as file:
        try:
            record_list_of_dicts = fileparse.parse_csv(file, 
                                                       select=['name', 'shares', 'price'], 
                                                       types=[str, int, float], 
                                                       has_header=True,
                                                       silence_errors=True)
        except TypeError as e:
            pass

    stocks_list_of_objects = [stock.Stock(**record_dict) for record_dict in record_list_of_dicts]
    # stocks_list_of_objects = [stock.Stock(record['name'], record['shares'],record['price']) for record in record_list_of_dicts]
    portfolio = Portfolio(stocks_list_of_objects) 
    
    # # Test portfolio object
    print(portfolio.total_cost)         # property
    print(portfolio.tabulate_shares())  # Method
    print(len(portfolio))
    print(portfolio[0])
    print(portfolio[0:3])
    print('GE' in portfolio)
    sys.exit(0)  # Exit to avoid further processing 
    
    
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

# Long version
# def print_report(report_list):
#     """ Print Report """
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # separator = '----------'
    # print("\n%10s %10s %-10s %10s" % headers)
    # print("%10s %10s %10s %10s" % (separator, separator, separator, separator))

    # for row in report_list:
    #     # unpack row tuple containing (name, shares, price, price_diff)
    #     print("%10s %10d $%-9.2f %10.2f" % row)

    # Tabulate report
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # print("\n%10s %10s %-10s %10s" % headers)
    # print(('-'*10 + ' ')*len(headers))

    # Using C-style formatting
    # Right-justified by default
    # Use - to left-justify
    # for row in report_list:
    #     # unpack row tuple containing (name, shares, price, price_diff)
    #     print("%10s %10d $%-9.2f %10.2f" % row)

    # # Or Using f-string for better readability
    # for name, shares, price, price_diff in report_list:
    #     print(f"{name:10} {shares:10} ${price:10.2f} {price_diff:10.2f}")

    # Counting and totalling shares: collections.Counter()
    # counter_dict = collections.Counter()
    # for row in report_list:
    #     counter_dict[row[0]] += row[1]

    # Reprint after filtering
    # sub_headers = headers[0], headers[1]
    # print("\n%10s %10s" % (sub_headers))
    # print(('-'*10 + ' ')*len(sub_headers))
    # for name, shares in counter_dict.items():
    #     print(f"{name:>10} {shares:>10}")

    # # Rank the totals
    # print(f'\n{counter_dict.most_common(3)=}')
    # return None

# Short version
def print_report(reportdata_list_of_tuples, table_formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    
    # Alternative: using a format string
    # headers = ('name', 'shares', 'price', 'change')
    # print('%10s %10s %10s %10s' % headers)
    # print(('-'*10 + ' ')*len(headers))
    # for rowdata in reportdata_list_of_tuples:
    #     print('%10s %10d %10.2f %10.2f' % rowdata)
    
    # Alternative: using the data as it is
    # headers = ('name', 'shares', 'price', 'change')
    # table_formatter.headings(headers)
    # for rowdata in reportdata_list_of_tuples:
    #     table_formatter.row(rowdata)
    
    # Alternative: casting ints and floats appropriately -> more readable
    # headers = ('name', 'shares', 'price', 'change')
    # table_formatter.headings(headers)
    # for name, shares, price, change in reportdata_list_of_tuples:
    #     rowdata = [name, int(shares), f"${float(price):.2f}", f"{float(change):.2f}"]
    #     table_formatter.row(rowdata)
    
    # Alternatively
    # Refactored to support DYNAMIC headers list, which work by calling tf.print_table()
    # Because we are using a report list, order must be preserved in headers
    # We couldn't switch to a dicts because all tableformat interfaces expects tuples
    select_headers = ('name', 'shares', 'price')
    headers = ('name', 'shares', 'price', 'change') # Original headers returned by make_report()
    indexes = [headers.index(head) for head in select_headers]
    table_formatter.headings(select_headers)
    for report in reportdata_list_of_tuples:
        report=list(report)  # Convert tuple to list for to allow modification
        report[1] = int(report[1])  
        report[2] = f"${float(report[2]):.2f}"
        report[3] = f"{float(report[3]):.2f}" 
        report = [report[i] for i in indexes]  # Filter data matching headers only
        tf.print_table(report, select_headers, table_formatter)
    

def portfolio_report(portfolio_filename,price_filename):
    """Main function to read data and generate report."""
  
    print(f"Reading prices from {price_filename} and portfolio from {portfolio_filename}...")
    
    # Instantiate one abstract base class to use
    # formatter = tf.TableFormatter
    # formatter = tf.TextTableFormatter()
    # formatter = tf.CSVTableFormatter()
    # formatter = tf.HTMLTableFormatter()
    
    # Print it out
    # fmt = 'html'  # Default format
    # if fmt == 'txt':
    #     formatter = tf.TextTableFormatter()
    # elif fmt == 'csv':
    #     formatter = tf.CSVTableFormatter()
    # elif fmt == 'html':
    #     formatter = tf.HTMLTableFormatter()
    # else:
    #     raise RuntimeError(f'Unknown format {fmt}')
    
    fmt = 'txt'  # Change to 'txt','csv' or 'html' as needed
    formatter = tf.create_formatter(fmt)
    
    price_list_of_dicts = read_prices(price_filename)
    portfolio_list_of_dicts = read_portfolio(portfolio_filename)
    print(f'{portfolio_list_of_dicts=}')

    if price_list_of_dicts and portfolio_list_of_dicts:
        report_list_of_tuples = make_report(portfolio_list_of_dicts, price_list_of_dicts)
        print(f'{report_list_of_tuples=}')
        if report_list_of_tuples:
            print_report(report_list_of_tuples, formatter)
        else:
            print("No matching data found in the report.")
    else:
        print("No data available to generate report.")
    return None


def main():
    # This segments shows up when running the script in the CLI using:
    # python3 report.py Data/portfolio.csv Data/prices.csv OR
    # python3 report.py "Data/portfolio.csv" "Data/prices.csv"
    
    # But not when imported as a module, using:
    # from report import portfolio_report
    # portfolio_report("Data/portfolio.csv", "Data/prices.csv")
    # NOTE: Running in REPL rejects 2_report.py as a module name, so use report.py
   
    # Check if the correct number of arguments are provided
    # sys.argv[0] is the script name, so we expect at least 3 arguments
    if len(sys.argv) < 3:
        print("Usage: python3 report.py <portfolio_file> <prices_file>")
        sys.exit(1)
        
    # Call the function with command line arguments
    portfolio_report(*sys.argv[1:])     # OR portfolio_report(sys.argv[1], sys.argv[2])
    
    # Confirm args numbering
    # [print(i, arg) for i,arg in enumerate(sys.argv)]
    # Output:
    # 0 report.py
    # 1 Data/portfolio.csv
    # 2 Data/prices.csv
    
    return None
    
if __name__ == "__main__":
    main()