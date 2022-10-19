#!/usr/bin/env python3

# ---------
# RangeT.py
# ---------

from unittest import main, TestCase

from Range import \
    range_1,      \
    range_2

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            range_1,
            range_2,
            range]

    def test_1 (self) :
        for f in self.a :
            x = f(2, 2)
            p = iter(x)
            self.assertIsNot(p, x)
            self.assertIs(iter(p), p)
            self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
            x = f(2, 3)
            p = iter(x)
            self.assertIsNot(p, x)
            self.assertIs(iter(p), p)
            self.assertEqual(next(p), 2)
            self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
            x = f(2, 4)
            p = iter(x)
            self.assertIsNot(p, x)
            self.assertIs(iter(p), p)
            self.assertEqual(next(p), 2)
            self.assertEqual(next(p), 3)
            self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
            x = f(2, 5)
            self.assertEqual(list(x), [2, 3, 4])
            self.assertEqual(list(x), [2, 3, 4])

if __name__ == "__main__" :
    main()