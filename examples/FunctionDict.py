#!/usr/bin/env python3

# ---------------
# FunctionDict.py
# ---------------

print("FunctionDict.py")

def f (x, y, **z) :
    return [x, y, z]

assert f(2, 3)               == [2, 3, {}]
assert f(2, 3, a = 4)        == [2, 3, {'a' : 4}]
assert f(2, 3, a = 4, b = 5) == [2, 3, {'a' : 4, 'b' : 5}]

d1 = {"b" : 4, "a" : 3}
assert f(2, 5,     **d1)  == [2, 5, {'a' : 3, 'b' : 4}]
assert f(2, y = 5, **d1)  == [2, 5, {'a' : 3, 'b' : 4}]
u = (2,)
assert f(y = 5, *u, **d1) == [2, 5, {'a' : 3, 'b' : 4}]
assert f(*u, y = 5, **d1) == [2, 5, {'a' : 3, 'b' : 4}]

d2 = {"y" : 3, "x" : 2}
assert f(**d2) == [2, 3, {}]

d3 = {"y" : 3}
assert f(2,     **d3) == [2, 3, {}]
assert f(x = 2, **d3) == [2, 3, {}]

d4 = {"y" : 3, "a" : 2}
assert f(2,     **d4) == [2, 3, {'a' : 2}]
assert f(x = 2, **d4) == [2, 3, {'a' : 2}]

print("Done.")
