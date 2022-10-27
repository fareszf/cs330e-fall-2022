#!/usr/bin/env python3

# -------------
# ThetaJoinT.py
# -------------

from unittest import main, TestCase

from ThetaJoin import    \
    theta_join_yield,    \
    theta_join_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            theta_join_yield,
            theta_join_generator]

        self.r = [
            {"A" : 1, "B" : 4},
            {"A" : 2, "B" : 5},
            {"A" : 3, "B" : 6}]

        self.s = [
            {"C" : 2, "D" : 7},
            {"C" : 3, "D" : 5},
            {"C" : 3, "D" : 6},
            {"C" : 4, "D" : 6}]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s, lambda u, v : False)),
                    [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s, lambda u, v : True)),
                    [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 5},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 6},
                     {'A': 1, 'B': 4, 'C': 4, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 2, 'D': 7},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 5},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 4, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 2, 'D': 7},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 4, 'D': 6}])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s, lambda u, v : u["A"] == v["C"])),
                    [{'A': 2, 'B': 5, 'C': 2, 'D': 7},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 6}])

if __name__ == "__main__" :
    main()
