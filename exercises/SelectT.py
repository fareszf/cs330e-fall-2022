#!/usr/bin/env python3

# ----------
# SelectT.py
# ----------

from unittest import main, TestCase

from Select import    \
    select_yield,     \
    select_generator, \
    select_filter

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            select_yield,
            select_generator,
            select_filter]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, lambda d : False)),
                    [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, lambda d : True)),
                    [{"A" : 1, "B" : 4, "C" : 3},
                     {"A" : 2, "B" : 5, "C" : 2},
                     {"A" : 3, "B" : 6, "C" : 1}])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, lambda d : d["B"] > 4)),
                    [{'A': 2, 'B': 5, 'C': 2},
                     {'A': 3, 'B': 6, 'C': 1}])

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, lambda d : d["A"] > d["C"])),
                    [{'A': 3, 'B': 6, 'C': 1}])

if __name__ == "__main__" :
    main()
