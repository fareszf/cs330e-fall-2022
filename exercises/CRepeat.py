from itertools import repeat

# ------
# CRepeat.py
# ------

# repeat(elem, [n]): Repeat will repeat an item endlessly or up to n (optional) times
class repeat_class() :
   def __init__(self, s, a = None) :
      self.s = s
      self.a = a
      self.counter = 0

   def __iter__(self) :
      return self
      
   def __next__(self) :
      if self.a is None :
         return self.s
      else :        
        self.counter += 1 
        if self.counter <= self.a:
            return self.s
        else:
            raise StopIteration         
            