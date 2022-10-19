#!/usr/bin/env python3

# ------
# CCount.py
# ------

# count(start, [step])
# ------------------------------
# Count starts counting up from a provided starting argument,
# optionally steps by provided step

class count_class() :
   def __init__(self, start, step = 1):
      self.start = start
      self.step = step

   def __iter__(self) :
      return self
      
   def __next__(self) :
      n = self.start
      self.start += self.step
      return n
      
