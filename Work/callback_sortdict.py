"""
By what criteria?
You can guide the sorting by using a key function. 
The key function is a function that receives the dictionary and 
returns the value of interest for sorting.

"""

import pprint


portfolio = [
    {"name": "MSFT", "price": 51.23, "shares": 200},
    {"name": "AA", "price": 32.2, "shares": 100},
    {"name": "GE", "price": 40.37, "shares": 95},
    {"name": "IBM", "price": 91.1, "shares": 50},
    {"name": "CAT", "price": 83.44, "shares": 150},
    {"name": "MSFT", "price": 65.1, "shares": 50},
    {"name": "IBM", "price": 70.44, "shares": 100}
]


# Callback functions
# These are functions that are passed as arguments to other functions.
# Callback functions are often short one-line functions that are only used for that one operation. 
def sort_by(s):
    return s["price"]

# The sort() method "calls back" to a function you supply. 
portfolio.sort(key=sort_by, reverse=True)  # .sort() sorts in place

# Or Using a lambda function
# portfolio.sort(key=lambda s: s["price"], reverse=True)

pprint.pprint(portfolio)
