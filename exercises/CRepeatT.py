# -------
# RepeatT.py
# -------

# https://docs.python.org/2/library/itertools.html#itertools.repeat

from unittest import main, TestCase
from CRepeat import repeat_class
from itertools import repeat

class MyUnitTests (TestCase) :
    def test_1 (self) :
       x = []
       for i in repeat_class(10) :
           if len(x) < 10 :
              x += [i]
           else:
               break
                
       self.assertEqual(x, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
       
    def test_2 (self) :
       x = []
       for i in repeat_class(10, 0) :
           if len(x) < 10 :
              x += [i]
           else:
               break
                
       self.assertEqual(x, [])

    def test_3 (self) :
       x = []
       for i in repeat_class(10, 1) :
           if len(x) < 10 :
              x += [i]
           else:
               break
       self.assertEqual(x, [10])

    def test_4 (self) :
       x = []
       for i in repeat_class(10, 20) :
           if len(x) < 10 :
              x += [i]
           else:
               break
       self.assertEqual(x, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])  
       
if __name__ == "__main__" :
    main()