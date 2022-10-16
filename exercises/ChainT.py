#!/usr/bin/env python3

# -------
# ChainT.py
# -------

# https://docs.python.org/2/library/itertools.html#itertools.chain

from unittest import main, TestCase
from itertools import chain
from Chain import    \
    chain_for, \
    chain_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            chain_for,
            chain_generator,
            chain]
        
    def test_1 (self) :
       for f in self.a :
            with self.subTest() :
                x = f([], [])
                self.assertEqual(list(x), [])      

    def test_2 (self) :
       for f in self.a :
            with self.subTest() :
                x = f(['A', 'B', 'C'], [])
                self.assertEqual(list(x), ['A', 'B', 'C'])

    def test_3 (self) :
       for f in self.a :
            with self.subTest() :
                x = f([], ['D', 'E', 'F'])
                self.assertEqual(list(x), ['D', 'E', 'F'])
                
    def test_4 (self) :
       for f in self.a :
            with self.subTest() :
                x = f(['A', 'B', 'C'], ['D', 'E', 'F'])
                self.assertEqual(list(x), ['A', 'B', 'C', 'D', 'E', 'F'])  
                
    def test_5 (self) :
       for f in self.a :
            with self.subTest() :
                x = f(['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'])
                self.assertEqual(list(x), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])  
    
if __name__ == "__main__" :
    main()