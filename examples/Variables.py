#!/usr/bin/env python3

# ------------
# Variables.py
# ------------

print("Variables.py")

i = 2
v = i
assert i is v
v += 1
assert i == 2
assert v == 3

a = [2, 3, 4]
b = a
assert a is b
b[1] += 1
assert a[1] == 4
assert a is b

a = (2, 3, 4)
b = a
assert a is b
#b[1] += 1    # TypeError: 'tuple' object does not support item assignment

a = [2, 3, 4]
b = a[:]
assert a is not b
assert a ==     b
b[1] += 1
assert a[1] == 3
assert b[1] == 4

a = (2, 3, 4)
b = a[:]
assert a is b

a = [2, 3, 4]
b = a
assert a is b
b += [5]
assert a == [2, 3, 4, 5]
assert a is b

a = [2, 3, 4]
b = a
assert a is b
b = b + [5]
assert a == [2, 3, 4]
assert b == [2, 3, 4, 5]

a = [2, 3, 4]
b = a
assert a is b
b += (5,)
assert a == [2, 3, 4, 5]
assert a is b

a = [2, 3, 4]
b = a
assert a is b
#b = b + (5,) # TypeError: can only concatenate list (not "tuple") to list

a = (2, 3, 4)
b = a
assert a is b
b += (5,)
assert a == (2, 3, 4)
assert b == (2, 3, 4, 5)

a = (2, 3, 4)
b = a
assert a is b
b = b + (5,)
assert a == (2, 3, 4)
assert b == (2, 3, 4, 5)

a = (2, 3, 4)
b = a
assert a is b
#b += [5]     # TypeError: can only concatenate tuple (not "list") to tuple

a = (2, 3, 4)
b = a
assert a is b
#b = b + [5]  # TypeError: can only concatenate tuple (not "list") to tuple

print("Done.")