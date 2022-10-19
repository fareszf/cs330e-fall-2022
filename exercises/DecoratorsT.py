#!/usr/bin/env python3

# --------------
# DecoratorsT.py
# --------------

from unittest import main, TestCase

from Decorators import \
    cache_1,           \
    cache_2

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

assert cycle_length( 1) == 1
assert cycle_length( 5) == 6
assert cycle_length(10) == 7

def cycle_length_1 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

def pre_gtz (f) :
    def g (n) :
        assert n > 0
        return f(n)
    return g

cycle_length_1 = pre_gtz(cycle_length_1)

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

def post_gtz (f) :
    def g (n) :
        v = f(n)
        assert v > 0
        return v
    return g

cycle_length_1 = post_gtz(cycle_length_1)

assert cycle_length_1( 1) == 1
assert cycle_length_1( 5) == 6
assert cycle_length_1(10) == 7

@cache_1
@pre_gtz
@post_gtz
def cycle_length_2 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

@cache_2
@pre_gtz
@post_gtz
def cycle_length_3 (n) :
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    return c

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            cycle_length_1,
            cycle_length_2,
            cycle_length_3]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(1), 1)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(5), 6)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(10), 7)

if __name__ == "__main__" :
    main()
