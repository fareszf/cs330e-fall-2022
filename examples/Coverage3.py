#!/usr/bin/env python3

# ------------
# Coverage3.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(3), 8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
$ coverage run --branch Coverage3.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



$ coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage3.py      16      0      4      0   100%
"""
