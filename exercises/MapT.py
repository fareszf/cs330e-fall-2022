#!/usr/bin/env python3

# -------
# MapT.py
# -------

# https://docs.python.org/3/library/functions.html#map

from timeit   import timeit
from unittest import main, TestCase

from Map import    \
    map_range_for, \
    map_for,       \
    map_while,  \
    map_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            map_range_for,
            map_for,
            map_while,
			map_generator,
            map]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 2, [])
                self.assertEqual(list(x), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 2, [2])
                self.assertEqual(list(x), [4])
                self.assertEqual(list(x), [])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 3, [2, 3])
                self.assertEqual(list(x), [8, 27])
                self.assertEqual(list(x), [])

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 2, [2, 3, 4])
                self.assertEqual(list(x), [4, 9, 16])
                self.assertEqual(list(x), [])

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                print()
                print(f.__name__)
                if f.__name__ == "map" :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda x : x ** 2, 10000 * [5]))",
                        "",
                        number = 100)
                else :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda x : x ** 2, 10000 * [5]))",
                        "from __main__ import " + f.__name__,
                        number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% MapT
....

map_range_for
384.34 milliseconds

map_for
317.92 milliseconds

map_while
C:\Python35-32\lib\timeit.py:6: PendingDeprecationWarning: generator 'map_while' raised StopIteration
  times.  See also Tim Peters' introduction to the Algorithms chapter in
380.87 milliseconds

map_generator
313.16 milliseconds

map
282.11 milliseconds
.
----------------------------------------------------------------------
Ran 5 tests in 1.684s

OK
"""
