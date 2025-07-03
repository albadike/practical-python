# Pytest 
# The 'assert' statement is an internal check for the program.

import simple

def test_add():
    "Test add with int args"
    assert simple.add(2,2) == 4

def test_str():
    """Test add with strings"""
    assert simple.add('hello','world') == 'helloworld'
    
def test_age():
    "Test age"
    assert isinstance(simple.age, int), "Expected int"
    
def test_cold():
    "Test cold"
    assert simple.is_cold == True, "It is cold" # assert <expression> [, 'Diagnostic message']