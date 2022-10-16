# -------
# CCycleT.py
# -------

# https://docs.python.org/2/library/itertools.html#itertools.cycle

from unittest import main, TestCase
from itertools import cycle
from CCycle import cycle_class

class MyUnitTests (TestCase) :
   def setUp (self) :
        self.a = [
            cycle_class,
            cycle]
 
   def test_1 (self) :
      for f in self.a :
         with self.subTest() :
            x = []
            for i in f([]):
               if len(x) < 10:
                  x += [i]
               else:
                  break
            self.assertEqual(x, [])    

   def test_2 (self) :
      for f in self.a :
         with self.subTest() :
            a = [1, 2, 3, 4]
            x = []
            for i in f(a):
               if len(x) < 10:
                  x += [i]
               else:
                  break    
            self.assertEqual(list(x), [1, 2, 3, 4, 1, 2, 3, 4, 1, 2])    
      
   def test_3 (self) :
       for f in self.a :
         with self.subTest() :
            a = 'ABCD'
            x = []
            for i in f(a):
               if len(x) < 10:
                  x += [i]
               else:
                  break
            self.assertEqual(list(x), ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B',])  

if __name__ == "__main__" :
    main()