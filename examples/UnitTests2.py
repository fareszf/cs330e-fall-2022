#!/usr/bin/env python3

# -------------
# UnitTests2.py
# -------------

# https://docs.python.org/3.6/library/unittest.html
# https://docs.python.org/3.6/library/unittest.html#assert-methods

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
    def test_1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 5)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
$ python UnitTests2.py
.F.
===========================================================
FAIL: test_2 (__main__.MyUnitTests)
-----------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests2.py", line 29, in test_2
    self.assertEqual(cycle_length( 5), 5)
AssertionError: 6 != 5

-----------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
"""