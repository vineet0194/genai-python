# method resolution order (MRO)

class A:
    label = "A: Class A"

class B(A):
    label = "B: Class B"

class C(A):
    label = "C: Class C"

class D(B, C):
    pass

obj = D()
print(obj.label)
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Python follows the MRO (Method Resolution Order), not just the inheritance tree.

# constructor also follow MRO (if you use super())