import collections

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]


## 1. collections.Counter 
counter = collections.Counter()
for name, shares, price in portfolio:
    counter[name] += shares

# print(f"{counter['IBM']=}")       # 150
print(f"{counter=}")                # counter=Counter({'GOOG': 175, 'IBM': 150, 'CAT': 150, 'AA': 50})
# print(counter.most_common(2))     # [('GOOG', 175), ('IBM', 150)]

# Also works, without using collections.Counter
my_dict = {}
for name, shares, price in portfolio:
    # print(f'{name=}')     # Last name in the portfolio is {}; hence my_dict[name] breaks down
                            # Another reason to always use a method if it exists
    
    # my_dict[name] = my_dict[name] + shares    # Produces the error below
    
    """
    name='GOOG'
Traceback (most recent call last):
  File "/Users/muhammal/Documents/practical-python/collections_.py", line 26, in <module>
    my_dict[name] = my_dict[name] + shares
                    ~~~~~~~^^^^^^
KeyError: 'GOOG'

REASON FOR ERROR: A dictionary key must be unique; collections.Counter() solves this problem easily.
UNANSWERED: Why is it breaking down on the first occurrence of 'GOOG'?
>>> {'goog':3, 'cat':5, 'goog':2}
{'goog': 2, 'cat': 5}
    """
    
    # Use the .get() method to avoid KeyError
    my_dict[name] = my_dict.get(name, 0) + shares
    
# print(f"{my_dict}")
print('=' * 100)


## 2. One-Many Mappings: collections.defaultdict
default_dict = collections.defaultdict(list)
print(default_dict)         # defaultdict(<class 'list'>, {})
print(type(default_dict))   # <class 'collections.defaultdict'>
print(default_dict[name])   # []  

for name, shares, price in portfolio:
    default_dict[name].append((shares, price))
print(f"{default_dict=}")  # default_dict=defaultdict(<class 'list'>, {'GOOG': [(100, 490.1), (75, 572.45)], 'IBM': [(50, 91.1), (100, 45.23)], 'CAT': [(150, 83.44)], 'AA': [(50, 23.15)]})

# Using defaultdict to sum shares
default_dict_sum = collections.defaultdict(int)
for name, shares, price in portfolio:
    default_dict_sum[name] += shares
print(f"{default_dict_sum=}")  # default_dict_sum=defaultdict(<class 'int'>, {'GOOG': 175, 'IBM': 150, 'CAT': 150, 'AA': 50})
print('=' * 100)


## 3. Create a history of the last N items: using collections.deque
filename = 'Work/Data/prices.csv'
N = 5  # Number of lines to keep in history
history = collections.deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
print(f"{history=}")  # history=deque(['"UTX",52.61\n', '"VZ",29.26\n', '"WMT",49.74\n', '"XOM",69.35\n', '\n'], maxlen=5)
# Accessing the last N lines
for line in history:
    print(line.strip())
# Output:
# "UTX",52.61
# "VZ",29.26
# "WMT",49.74
# "XOM",69.35
print('=' * 100)


## 4. One-Many Mappings: collections.namedtuple
Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])
portfolio_namedtuple = [
    Stock('GOOG', 100, 490.1),
    Stock('IBM', 50, 91.1),
    Stock('CAT', 150, 83.44),
    Stock('IBM', 100, 45.23),
    Stock('GOOG', 75, 572.45),
    Stock('AA', 50, 23.15)
]
# Accessing namedtuple fields
for stock in portfolio_namedtuple:
    print(f"{stock.name=}, {stock.shares=}, {stock.price=}")
# Output:
# stock.name='GOOG', stock.shares=100, stock.price=490.1
# stock.name='IBM', stock.shares=50, stock.price=91.1
# stock.name='CAT', stock.shares=150, stock.price=83.44
# stock.name='IBM', stock.shares=100, stock.price=45.23
# stock.name='GOOG', stock.shares=75, stock.price=572.45
# stock.name='AA', stock.shares=50, stock.price=23.15
print('=' * 100)


## 5. collections.OrderedDict
ordered_dict = collections.OrderedDict()
for name, shares, price in portfolio:
    ordered_dict[name] = ordered_dict.get(name, 0) + shares
print(f"{ordered_dict=}")  # ordered_dict=OrderedDict([('GOOG', 175), ('IBM', 150), ('CAT', 150), ('AA', 50)])
# OrderedDict maintains the order of insertion
# Accessing items in OrderedDict
for name, shares in ordered_dict.items():
    print(f"{name=}, {shares=}")
# Output:
# name='GOOG', shares=175
# name='IBM', shares=150
# name='CAT', shares=150
# name='AA', shares=50
print('=' * 100)


## 6. collections.ChainMap
chain_map = collections.ChainMap()
# Creating two dictionaries to demonstrate ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain_map = collections.ChainMap(dict1, dict2)
print(f"{chain_map=}")  # chain_map=ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
# Accessing items in ChainMap
for key in chain_map:
    print(f"{key=}, {chain_map[key]=}")
# Output:
# key='a', chain_map[key]=1
# key='b', chain_map[key]=2
# key='c', chain_map[key]=4
# ChainMap allows you to group multiple dictionaries together
# and access them as a single mapping.
# It also allows you to update the values in the first dictionary
# in the ChainMap, which will reflect in the ChainMap.
# Updating a value in the first dictionary
dict1['a'] = 10
print(f"{chain_map=}")  # chain_map=ChainMap({'a': 10, 'b': 2}, {'b': 3, 'c': 4})
# Accessing updated value
print(f"{chain_map['a']=}")  # chain_map['a']=10

# ChainMap is useful for managing multiple contexts or scopes,
# such as when dealing with configuration settings or nested scopes.
# It allows you to easily switch between different contexts
# without having to create new dictionaries or data structures.
# ChainMap can also be used to merge multiple dictionaries
# without losing the original dictionaries, making it a powerful tool
# for managing complex data structures.
# ChainMap can also be used to create a view of multiple dictionaries
# without modifying the original dictionaries, allowing you to
# create a read-only view of the data.
# This can be useful for creating a snapshot of the data
# at a specific point in time, or for creating a view of the data
# that can be shared with other parts of the code without
# modifying the original data.
# ChainMap can also be used to create a view of multiple dictionaries  
