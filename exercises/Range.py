#!/usr/bin/env python3

# --------
# Range.py
# --------

class range_1 :
    class iterator () :
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

    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return range_1.iterator(self.b, self.e)

class range_2 :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        b = self.b
        e = self.e
        while b != e :
            yield b
            b += 1