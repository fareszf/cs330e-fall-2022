#!/usr/bin/env python3

# -------
# Copy.py
# -------

from copy import copy, deepcopy

print("Copy.py")

x = [2, 3, 4]
y = [1, x, 5]

z = y[:]
assert y    is not z
assert y    ==     z
assert y[1] is     z[1]

z = copy(y)
assert y    is not z
assert y    ==     z
assert y[1] is     z[1]

z = deepcopy(y)
assert y    is not z
assert y    ==     z
assert y[1] is not z[1]
assert y[1] ==     z[1]

print("Done.")