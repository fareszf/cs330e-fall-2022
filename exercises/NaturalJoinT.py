#!/usr/bin/env python3

# ---------------
# NaturalJoinT.py
# ---------------

from unittest import main, TestCase

from NaturalJoin import      \
    natural_join_yield,      \
    natural_join_generator,  \
    natural_join_theta_join

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            natural_join_yield,
            natural_join_generator,
            natural_join_theta_join]
        self.r = []
        self.s = []

    def test_1 (self) :
        self.r = [
            {"A" : 1, "B" : 4},
            {"A" : 2, "B" : 5},
            {"A" : 3, "B" : 6}]

        self.s = [
            {"C" : 2, "D" : 7},
            {"C" : 3, "D" : 5},
            {"C" : 3, "D" : 6},
            {"C" : 4, "D" : 6}]

        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s)),
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

    def test_2 (self) :
        self.r = [
            {"A" : 1, "B" : 4, "C" : 7},
            {"A" : 2, "B" : 5, "C" : 8},
            {"A" : 3, "B" : 6, "C" : 9}]

        self.s = [
            {"A" : 4, "B" : 4, "D" : 7},
            {"A" : 5, "B" : 5, "D" : 5},
            {"A" : 6, "B" : 6, "D" : 6},
            {"A" : 7, "B" : 7, "D" : 6}]

        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s)),
                    [])

    def test_3 (self) :
        self.r = [
            {"A" : 1, "B" : 4, "C" : 7},
            {"A" : 2, "B" : 5, "C" : 8},
            {"A" : 3, "B" : 6, "C" : 9}]

        self.s = [
            {"A" : 2, "B" : 4, "D" : 7},
            {"A" : 3, "B" : 5, "D" : 5},
            {"A" : 3, "B" : 6, "D" : 6},
            {"A" : 4, "B" : 7, "D" : 6}]

        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s)),
                    [{'A': 3, 'B': 6, 'C': 9, 'D': 6}])

if __name__ == "__main__" :
    main()
