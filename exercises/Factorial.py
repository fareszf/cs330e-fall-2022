#!/usr/bin/env python3

# ------------
# Factorial.py
# ------------

# https://docs.python.org/3.6/library/math.html

from functools import reduce
from operator  import mul

# recursive procedure
# linear recursive process
def factorial_recursion (n) :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

# recursive procedure
# linear iterative process
def factorial_tail_recursion (n) :
    assert n >= 0
    def f (n, v) :
        assert n >= 0
        assert v >= 1
        if n < 2 :
            return v
        return f(n - 1 , n * v)
    return f(n, 1)

# iterative procedure
# linear iterative process
def factorial_while (n) :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_range_for (n) :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

def factorial_range_reduce (n) :
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)
