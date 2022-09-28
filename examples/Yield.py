#!/usr/bin/env python3

# --------
# Yield.py
# --------

print("Yield.py")

def f () :
    yield 2
    yield 3
    yield 4

p = f()
n = next(p)
assert n == 2
n = next(p)
assert n == 3
n = next(p)
assert n == 4
try :
    n = next(p)
except StopIteration :
    pass

p = f()
assert list(p) == [2, 3, 4]
assert list(p) == []

p = f()
assert list(p) == [2, 3, 4]

def g () :
    for v in [2, 3, 4] :
        yield v

p = g()
n = next(p)
assert n == 2
n = next(p)
assert n == 3
n = next(p)
assert n == 4
try :
    n = next(p)
except StopIteration :
    pass

print("Done.")
