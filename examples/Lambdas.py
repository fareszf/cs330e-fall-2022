#!/usr/bin/env python3

#pylint: disable = bad-builtin, function-redefined

# ----------
# Lambdas.py
# ----------

from functools import reduce

print("Lambdas.py")

def my_function (x, y) :
    return x + y

bf = my_function

assert my_function(2, 3) == 5
assert          bf(2, 3) == 5

assert reduce(my_function, [2, 3, 4], 0) == 9
assert reduce(bf,          [2, 3, 4], 0) == 9



bf = lambda x, y : x + y

assert (lambda x, y : x + y)(2, 3) == 5
assert bf(2, 3)                    == 5

assert reduce(lambda x, y : x + y, [2, 3, 4], 0) == 9
assert reduce(bf,                  [2, 3, 4], 0) == 9



def my_function () :
    def f (x, y) :
        return x + y
    return f

bf = my_function()

assert my_function()(2, 3) == 5
assert            bf(2, 3) == 5

assert reduce(my_function(), [2, 3, 4], 0) == 9
assert reduce(bf,            [2, 3, 4], 0) == 9



def my_lambda () :
    return lambda x, y : x + y

bf = my_lambda()

assert my_lambda()(2, 3) == 5
assert          bf(2, 3) == 5

assert reduce(my_lambda(), [2, 3, 4], 0) == 9
assert reduce(bf,          [2, 3, 4], 0) == 9



def my_closure (x) :
    def f (y) :
        return x + y
    return f

uf = my_closure(2)

assert my_closure(2)(3) == 5
assert            uf(3) == 5

assert list(map(my_closure(2), [2, 3, 4])) == [4, 5, 6]
assert list(map(uf,            [2, 3, 4])) == [4, 5, 6]



def my_closure (x) :
    return lambda y : x + y

uf = my_closure(2)

assert my_closure(2)(3) == 5
assert            uf(3) == 5

assert list(map(my_closure(2), [2, 3, 4])) == [4, 5, 6]
assert list(map(uf,            [2, 3, 4])) == [4, 5, 6]

print("Done.")