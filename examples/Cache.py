#!/usr/bin/env python3

# --------
# Cache.py
# --------

print("Cache.py")

x = 2
y = 2 + 0
assert x is y

x = 257
y = 257
assert x is y

x = 257            # cache: [-5, 256]
y = 257 + 0
assert x is not y
assert x ==     y
x -= 1
assert x is not y
assert x !=     y
y -= 1
assert x is y

x = -6             # cache: [-5, 256]
y = -6 + 0
assert x is not y
assert x ==     y
x += 1
assert x is not y
assert x !=     y
y += 1
assert x is y

x = 2.34
y = 2.34
assert x is y

x = 2.34
y = 2.34 + 0
assert x is not y
assert x ==     y

s = "abc"
t = "abc"
assert s is t

s = "abc"
t = "ab" + "c"
assert s is t

s = "abc"
u = "ab"
v = "c"
t = u + v
assert s is not t
assert s ==     t

a = []
b = []
assert a is not b
assert a ==     b

a = ()
b = ()
assert a is b

a = set()
b = set()
assert a is not b
assert a ==     b

a = frozenset()
b = frozenset()
assert a is b

a = {}
b = {}
assert a is not b
assert a ==     b

print("Done.")