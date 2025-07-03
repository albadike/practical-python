# testing

"""
RELATIVE imports use a dot (.) notation to specify the path to the module 
    relative to the current module's location within the package.
A single dot (.) represents the current package.
Two dots (..) represent the parent package.

# In module2.py within the package:
from .module1 import function1     # This will import function1 from module1 in the same package

Limitations:
- Can only be used within a package: You cannot use relative imports in a script executed as the main module.
- Can become confusing: In deeply nested package structures, they can become confusing.

Alternative: ABSOLUTE Imports
Syntax: Absolute imports specify the full path from the project's root to the module being imported.

from my_package.module1 import function1    # my_package is the top-level package

Benefits:
Clarity: Clearly indicates the location of imported modules, especially useful in large projects.
Stability: Less prone to errors in a changing codebase.
Avoids naming conflicts: Lower risk of accidentally importing a different module with the same name.

**Recommended: PEP 8 (the Python Style Guide) recommends absolute imports. 

"""

from TestPackage.fileparses import parse_csv
from TestPackage.fileparses import print_greetings

def calculate_portfolio_cost(portfolio):
    total_cost = 0.0
    for stock in portfolio:
        total_cost += stock['shares'] * stock['price']
    return total_cost