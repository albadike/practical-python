
obj = [1,2,3,4]

# All the objects that work with the for-loop implement this low-level iteration protocol.
_iter = obj.__iter__()     
while True:
    try:
        x = _iter.__next__() 
        print(x)
    except StopIteration:     # No more items
        break
    
# getattr()
# getattr(object, name[, default]) -> value
# Equivalent to object.name