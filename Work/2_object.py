"""

>>> a = [1,2,3]
>>> b=a
>>> id(a)
4410255680
>>> id(b)
4410255680
>>> a==b
True
>>> b==a
True
>>> a is b
True
>>> b is a
True

# Shallow copy: using list()
>>> a = [2,3,[100,101],4]
>>> id(a)
4410264384
>>> b=list(a)
>>> id(b)
4409953792
>>> a is b
False
>>> a == b
True
>>> a
[2, 3, [100, 101], 4]
>>> b
[2, 3, [100, 101], 4]
>>> list(b)
[2, 3, [100, 101], 4]
>>> a==b
True
>>> a is b
False

>>> a[2].append(102)
>>> a
[2, 3, [100, 101, 102], 4]
>>> b
[2, 3, [100, 101, 102], 4]
>>> a.append(5)
>>> a
[2, 3, [100, 101, 102], 4, 5]
>>> b
[2, 3, [100, 101, 102], 4]

# List and Dict have .copy() method
>>> a.
a.append(    a.copy()     a.extend(    a.insert(    a.remove(    a.sort(      
a.clear()    a.count(     a.index(     a.pop(       a.reverse()  
>>> my_dict={2:'a', 3:'b'}
>>> my_dict.
my_dict.clear(       my_dict.fromkeys(    my_dict.items(       my_dict.pop(         my_dict.setdefault(  my_dict.values(
my_dict.copy(        my_dict.get(         my_dict.keys(        my_dict.popitem()    my_dict.update(      

# Shallow copy 2 using [:]
>>> a
[2, 3, [100, 101, 102], 4, 5]
>>> p=a[:]
>>> a
[2, 3, [100, 101, 102], 4, 5]
>>> p
[2, 3, [100, 101, 102], 4, 5]
>>> a[2].append(555)
>>> a
[2, 3, [100, 101, 102, 555], 4, 5]
>>> p
[2, 3, [100, 101, 102, 555], 4, 5]

# Deep copy: using copy.deepcopy()
>>> import copy
>>> a
[2, 3, [100, 101, 102, 555], 4, 5]
>>> copy.
copy.Error(          copy.copy(           copy.deepcopy(       copy.dispatch_table  copy.error(          
>>> q=copy.deepcopy(a)
>>> a
[2, 3, [100, 101, 102, 555], 4, 5]
>>> q
[2, 3, [100, 101, 102, 555], 4, 5]
>>> a[2].append(9999)   
>>> a
[2, 3, [100, 101, 102, 555, 9999], 4, 5]
>>> q
[2, 3, [100, 101, 102, 555], 4, 5]

"""


import csv
import pprint


with open('Work/Data/dowstocks.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = next(reader)
print(f'{headers=}')
print(f'{rows=}')
print('--')

types = [str, float, str, str, float, float, float, float, int]
records = {head: func(val) for head, func, val in zip(headers, types, rows)}
print(f"{records=}")
print('--') 
pprint.pprint(f"records {records}") # Note pprint() returns ("records")