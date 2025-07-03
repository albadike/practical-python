"""
Managed attributes.

Accessor methods (getters and setters) in Python.
They are used to control access to class attributes.
"""

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        # Creates private attribute 'self._shares' here
        self.set_shares(shares)
        self.price = price

    # Function that layers the "get" operation
    def get_shares(self):
        return self._shares

    # Function that layers the "set" operation
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value

    def what_is_this(self):
        self._new_variable = 'This is a new variable'   # INVALID in Python


stock = Stock('ACME', 100, 123.45)

# Accessing the shares using the getter
print(stock.get_shares())  # Output: 100

# Setting the shares using the setter
stock.set_shares(200)
print(stock.get_shares())  # Output: 200

# Direct access to the shares attribute is possible but DISCOURAGED
print(stock._shares)    # Output: 200

# Testing the setter with an invalid type
try:
    stock.set_shares('two hundred')  # Raises TypeError
except TypeError as e:
    print(f'**Error: ', e)

# Accessing the new variable
print(stock.what_is_this())     # Returns 'None'. REASON: Runs ok since it is a normal method
# print(stock._new_variable)    # Raises AttributeError. REASON: You cannot create a self attribute '_new_variable' on the fly
# print(stock.shares)           # Raises AttributeError. REASON: 'self.shares' does not exist in the class
