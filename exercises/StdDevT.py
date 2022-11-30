#!/usr/bin/env python3

# ---------
# StdDevT.py
# ---------

# http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html

from statistics import StatisticsError
from timeit     import timeit
from unittest   import main, TestCase

from StdDev import    \
    stdev_range_for, \
    stdev_for,       \
    stdev_reduce,    \
    stdev_map,       \
    stdev_list,      \
    stdev_generator, \
    stdev_numpy

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            stdev_range_for,
            stdev_for,
            stdev_reduce,
            stdev_map,
            stdev_list,
            stdev_generator,
            stdev_numpy]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f([2, 2]), 0)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f([2, 3]), 0.7071067811865476)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f([2, 2, 2]), 0)

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f([2, 3, 4]), 1)

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertRaises(StatisticsError, f, [])

    def test_6 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertRaises(StatisticsError, f, [2])

    def test_7 (self) :
        for f in self.a :
            with self.subTest() :
                print()
                print(f.__name__)
                t = timeit(f.__name__ + "(10000 * [2]) == 0", "from __main__ import " + f.__name__, number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" :
    main()

"""
% StDevT
......
stdev_range_for
772.84 milliseconds
stdev_for
669.91 milliseconds
stdev_reduce
748.79 milliseconds
stdev_map
768.83 milliseconds
stdev_list
670.58 milliseconds
stdev_generator
699.25 milliseconds
stdev_numpy
65.02 milliseconds
.
----------------------------------------------------------------------
Ran 5 tests in 4.323s
OK
"""