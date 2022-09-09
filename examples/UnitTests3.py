#!/usr/bin/env python3

# -------------
# UnitTests3.py
# -------------

# https://docs.python.org/3.6/library/unittest.html
# https://docs.python.org/3.6/library/unittest.html#assert-methods

from unittest import main, TestCase

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

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
$ python UnitTests3.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""