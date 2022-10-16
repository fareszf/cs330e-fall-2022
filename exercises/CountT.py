#!/usr/bin/env python3

# -------
# CountT.py
# -------

# https://docs.python.org/2/library/itertools.html#itertools.count

from unittest import main, TestCase
from itertools import count
from Count import count_while

class MyUnitTests (TestCase) :
    def test_1 (self) :
        x = []
        for i in count_while(10) :
            if i < 15 :
                x += [i]
            else :
                break
        self.assertEqual(x, [10, 11, 12, 13, 14]) 

    def test_2 (self) :
        x = []
        for i in count_while(10, 2) :
           if i < 15 :
              x += [i]
           else :
              break
        self.assertEqual(x, [10, 12, 14])

    def test_3 (self) :
       x = []
       for i in count_while(10, 0.5) :
          if i < 15 :
             x += [i]
          else :
             break
       self.assertEqual(x, [10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5])
       
    def test_4 (self) : 
       x = []     
       for i in count_while(10, -0.5):
          if i > 5:
             x += [i]
          else:
             break
       self.assertEqual(x, [10, 9.5, 9.0, 8.5, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5])
        
if __name__ == "__main__" :
   main()
