# testing

"""
They both breaks the code if the module is run as a script directly 
e.g. python3 TestPackage/reports.py
ImportError: attempted relative import with no known parent package OR
ModuleNotFoundError: No module named 'TestPackage'

Solution: Use -m switch to run the module as a script 
e.g. python3 -m TestPackage.reports
"""

# . and TestPackage are both valid and equivalent
from . import fileparses    


def read_portfolio(filename):
    return fileparses.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float], has_header=True)

greet = fileparses.print_greetings(['Alice', 'Bob', 'Charlie'])
print(greet)