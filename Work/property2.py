"""
It should be noted that __slots__ is most commonly used as an optimization on classes that serve as data structures. 
Using slots will make such programs use far-less memory and run a bit faster. 
You should probably avoid __slots__ on most other classes however.
"""
    
class Stock:
    __slots__ = ('name', '_shares', 'price')  # '__slots__' freezes the attribute collection; can be list, tuple, or dict
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares        # Works even without modifying to 'self._shares'
        self.price = price
        # self.age = 60             # AttributeError. Creation unsuccessful because of __slots__

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value


stock = Stock('ACME', 100, 123.45)

# Getter
print(f"stock.shares = {stock.shares}")  # Output: 100

# Setter
stock.shares = 75
print(f"After calling setter, stock.shares = {stock.shares}")  # Output: 75

# print(f"stock._shares= {stock.age}")  # AttributeError. Cannot add new attributes to the class due to __slots__

# print(stock.__dict__)  # AttributeError: 'Stock' object has no attribute '__dict__'.