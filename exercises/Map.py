#!/usr/bin/env python3

#pylint: disable = consider-using-enumerate, too-few-public-methods

# ------
# Map.py
# ------

def map_range_for (uf, a) :
    for i in range(len(a)) :
        yield uf(a[i])

def map_for (uf, a) :
    for v in a :
        yield uf(v)

def map_while (uf, a) :
    p = iter(a)
    try:
       while True : 
           yield uf(next(p))
    except StopIteration:
       return
       	
def map_generator (uf, a) :
    return (uf(v) for v in a)
