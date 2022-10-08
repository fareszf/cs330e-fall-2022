#!/usr/bin/env python3

#pylint: disable = dangerous-default-value

# -------------------
# FunctionDefaults.py
# -------------------

print("FunctionDefaults.py")

def f (x, y, z = 4) :
    return [x, y, z]

assert f(2, 3)    == [2, 3, 4]
assert f(2, 3, 5) == [2, 3, 5]

# def g (x, y = 3, z) : # SyntaxError: non-default argument follows default argument
#     return [x, y, z]

def g (x = 2, y = 3, z = 4) :
    return [x, y, z]

assert g()         == [2, 3, 4]
assert g(5)        == [5, 3, 4]
assert g(5, 6)     == [5, 6, 4]
assert g(5, 6, 7)  == [5, 6, 7]
assert g(5, z = 7) == [5, 3, 7]



def h1 (x = []) : # mutable default
    x += [2]
    return x

assert h1()    == [2]
assert h1()    == [2, 2]
assert h1([1]) == [1, 2]
assert h1()    == [2, 2, 2]
assert h1([1]) == [1, 2]



def h2 (x = ()) : # immutable default
    x += (2,)
    return x

assert h2()     == (2,)
assert h2()     == (2,)
assert h2((1,)) == (1, 2)
assert h2()     == (2,)
assert h2((1,)) == (1, 2)



def h3 (x = None) :
    if x is None :
        x = []
    x += [2]
    return x

assert h3()     == [2]
assert h3()     == [2]
assert h3([1])  == [1, 2]
assert h3()     == [2]
assert h3([1])  == [1, 2]
assert h3(None) == [2]

print("Done.")
