# Single inheritance hierarchy test for class.__bases__

# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B): pass
# class E(D): pass

# Multiple inheritance hierarchy test for class.__bases__

class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): name = 'Extended'
