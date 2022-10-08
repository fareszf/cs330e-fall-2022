#!/usr/bin/env python3

# ----------------
# FunctionTuple.py
# ----------------

print("FunctionTuple.py")

def f (x, y, *z) :
    return [x, y, z]

assert f(2, 3)       == [2, 3, ()]
assert f(2, 3, 4)    == [2, 3, (4,)]
assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

t = (3, 4)
assert f(2, 5,  t)  == [2, 5, ((3, 4),)]
assert f(2, 5, *t)  == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, (4,)]
assert f(*t)        == [3, 4, ()]

u = (2,)
assert f(y = 3, *u) == [2, 3, ()]
assert f(*u, y = 3) == [2, 3, ()]

d1 = {"y" : 3, "x" : 2}
assert f(**d1) == [2, 3, ()]

d2 = {"y" : 3}
assert f(2,     **d2) == [2, 3, ()]
assert f(x = 2, **d2) == [2, 3, ()]

print("Done.")
