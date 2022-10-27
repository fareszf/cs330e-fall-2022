#!/usr/bin/env python3

#pylint: disable = bad-builtin, no-name-in-module, redefined-variable-type, too-few-public-methods

# ------------
# Functions.py
# ------------

from types import FunctionType, LambdaType, MethodType

print("Functions.py")

def inc_1 (i) :
    return i + 1

assert isinstance(inc_1, FunctionType)
assert hasattr(inc_1, "__call__")

assert inc_1(2)                    == 3         # function invocation; self -> undefined
assert list(map(inc_1, [2, 3, 4])) == [3, 4, 5] # function invocation; self -> undefined

a = [2]
assert inc_1(*a) == 3 # apply invocation; self -> undefined



inc_2 = lambda i : i + 1
assert isinstance(inc_2, LambdaType)
assert hasattr(inc_2, "__call__")

assert inc_2(2)                    == 3         # function invocation; self -> undefined
assert list(map(inc_2, [2, 3, 4])) == [3, 4, 5] # function invocation; self -> undefined

a = [2]
assert inc_2(*a) == 3 # apply invocation; self -> undefined



def make_inc_a () :
    return lambda i : i + 1

inc_3 = make_inc_a()
assert isinstance(inc_3, LambdaType)
assert hasattr(inc_3, "__call__")

assert inc_3(2)                    == 3         # function invocation; self -> undefined
assert list(map(inc_3, [2, 3, 4])) == [3, 4, 5] # function invocation; self -> undefined

a = [2]
assert inc_3(*a) == 3 # apply invocation; self -> undefined



def make_inc_b (j) :
    return lambda i : i + j

inc_4 = make_inc_b(1)
assert isinstance(inc_4, LambdaType)
assert hasattr(inc_4, "__call__")

assert inc_4(2)                    == 3         # function invocation; self -> undefined
assert list(map(inc_4, [2, 3, 4])) == [3, 4, 5] # function invocation; self -> undefined

a = [2]
assert inc_4(*a) == 3 # apply invocation; self -> undefined



class A (object) :
    def __init__ (self, j) :
        self.j = j

    def inc (self, i) :
        return i + self.j

x = A(1)
assert isinstance(x, A)

inc_5 = x.inc
assert isinstance(inc_5, MethodType)

assert inc_5(2)                    == 3         # function invocation; self -> x
assert list(map(inc_5, [2, 3, 4])) == [3, 4, 5] # function invocation; self -> x

a = [2]
assert inc_5(*a) == 3 # apply invocation; self -> x



inc_6 = A.inc
assert isinstance(inc_6, FunctionType)

assert inc_6(x, 2)                                  == 3         # function invocation; self -> x
assert list(map(lambda y : inc_6(x, y), [2, 3, 4])) == [3, 4, 5] # function invocation; self -> x

a = [x, 2]
assert inc_6(*a) == 3 # apply invocation; self -> x



class B (object) :
    def __init__ (self, j) :
        self.j = j

    def __call__ (self, i) :
        return i + self.j

inc_7 = B(1)
assert isinstance(inc_7, B)
assert hasattr(inc_7, "__call__")

assert inc_7(2)                    == 3         # object invocation; self -> inc_7
assert list(map(inc_7, [2, 3, 4])) == [3, 4, 5] # object invocation; self -> inc_7

a = [2]
assert inc_7(*a) == 3 # apply invocation; self -> inc_7

print("Done.")
