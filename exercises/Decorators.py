#!/usr/bin/env python3

#pylint: disable = too-few-public-methods

# -------------
# Decorators.py
# -------------

def cache_1 (f) :
    d = {}
    def g (n) :
        if n not in d :
            d[n] = f(n)
        return d[n]
    return g

class cache_2 :
    def __init__ (self, f) :
        self.f = f
        self.d = {}

    def __call__ (self, n) :
        if n not in self.d :
            self.d[n] = self.f(n)
        return self.d[n]
