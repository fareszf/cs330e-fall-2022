#!/usr/bin/env python3

# ----------
# ReduceT.py
# ----------

# https://docs.python.org/3/library/functools.html

from functools import reduce
from operator  import add, sub
from unittest  import main, TestCase

from Reduce import    \
    reduce_for_range, \
    reduce_for,       \
    reduce_while

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            reduce_for_range,
            reduce_for,
            reduce_while,
            reduce]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(None, [],       0),  0)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [2],       1),  3)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [2, 3, 4], 0),  9)

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 0), -9)

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 1), -8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% ReduceT
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
"""
