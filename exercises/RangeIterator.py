#!/usr/bin/env python3

#pylint: disable = too-few-public-methods

# ----------------
# RangeIterator.py
# ----------------

class Range_Iterator () :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return self

    def __next__ (self) :
        if self.b == self.e :
            raise StopIteration()
        v = self.b
        self.b += 1
        return v

def range_iterator_while (b, e) :
    while b != e :
        yield b
        b += 1
