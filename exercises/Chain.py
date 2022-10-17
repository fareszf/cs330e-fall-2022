#!/usr/bin/env python3

# ------
# Chain.py
# ------

# chain(iter1, iter2, ...)
# -----------------
# Chain make an iterator that returns elements from the first iterable
# until it is exhausted, then proceeds to the next iterable, until all
# of the iterables are exhausted.
# Used for treating consecutive sequences as a single sequence

def chain_for(*a) :
    if a :
       for i in a :
          for j in i :
             yield j
    else :
       pass    
       
def chain_generator(*a) :
   if a :
      return (j for i in a for j in i)
   else :
      pass