#!/usr/bin/env python3

# -----------
# ProjectT.py
# -----------

from unittest import main, TestCase

from Project import        \
    project_yield,         \
    project_comprehension, \
    project_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            project_yield,
            project_comprehension,
            project_generator]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, "D")),
                    [{}, {}, {}])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, "B")),
                    [{'B': 4},
                     {'B': 5},
                     {'B': 6}])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, "A", "C")),
                    [{'A': 1, 'C': 3},
                     {'A': 2, 'C': 2},
                     {'A': 3, 'C': 1}])

if __name__ == "__main__" :
    main()
