#!/usr/bin/env python3

#pylint: disable = redefined-variable-type

# -------------
# Indexables.py
# -------------

from itertools import count

print("Iteration.py")

a = [2, 3, 4]                     # list
assert isinstance(a, list)
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
s = 0
for v in a :
    s += v
assert s == 9

a = (2, 3, 4)                     # tuple
assert isinstance(a, tuple)
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
s = 0
for v in a :
    s += v
assert s == 9

a = [2, 3, 4]
for v in a :
    v += 1            # ?
assert a == [2, 3, 4]

a = [[2], [3], [4]]
for v in a :
    v += (5,)                        # ?
assert a == [[2, 5], [3, 5], [4, 5]]

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)                  # ?
assert a == [(2,), (3,), (4,)]

a = ["abc", "def", "ghi"]
for v in a :
    v += "x"                      # ?
assert a == ["abc", "def", "ghi"]

a = ["abc", "def", "ghi"]
s = ""
for v in a :
    s += v
assert s == "abcdefghi"

a = [[2, "abc"], [3, "def"], [4, "ghi"]]
s = 0
for u, v in a :
    s += u
assert s == 9

a = [(2, "abc"), (3, "def"), (4, "ghi")]
s = 0
for u, v in a :
    s += u
assert s == 9

a = {2, 3, 4}                     # set
assert isinstance(a, set)
assert not hasattr(a, "__next__")
assert     hasattr(a, "__iter__")
s = 0
for v in a :                      # order not guaranteed
    s += v
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"} # dict
assert isinstance(d, dict)
assert not hasattr(d, "__next__")
assert     hasattr(d, "__iter__")
s = 0
for k in d :                          # order not guaranteed
    s += k
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"}
k = d.keys()
assert str(type(k)) == "<class 'dict_keys'>"
assert set(k) == {2, 3, 4}
assert set(k) == {2, 3, 4}

d = {2 : "abc", 3 : "def", 4 : "ghi"}
v = d.values()
assert str(type(v)) == "<class 'dict_values'>"
assert set(v) == {"abc", "def", "ghi"}
assert set(v) == {"abc", "def", "ghi"}

d = {2 : "abc", 3 : "def", 4 : "ghi"}
kv = d.items()
assert str(type(kv)) == "<class 'dict_items'>"
assert set(kv) == {(2, "abc"), (3, "def"), (4, "ghi")}
assert set(kv) == {(2, "abc"), (3, "def"), (4, "ghi")}

x = range(10)
assert isinstance(x, range)
assert not hasattr(x, "__next__")
assert     hasattr(x, "__iter__")
assert list(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert list(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = range(2, 10)
assert list(x) == [2, 3, 4, 5, 6, 7, 8, 9]

x = range(2, 10, 2)
assert list(x) == [2, 4, 6, 8]

x = range(10, 2, -2)
assert list(x) == [10, 8, 6, 4]

x = range(10)
assert hasattr(x, "__getitem__")
assert x[0] == 0
assert x[9] == 9
try :
    assert x[10] == 10 # error: out of range
    assert False
except IndexError :
    pass
#x[0] = 2              # TypeError: 'xrange' object does not support item assignment
s = 0
for v in x :
    s += v
assert s == 45
s = 0
for v in x :
    s += v
assert s == 45

x = range(15)
s = 0
for v in x :
    if v == 10 :
        break
    s += v
else :           # else clause in a for loop
    assert False # executes when the loop terminates normally
assert s == 45

x = count(0)                         # 0, 1, 2, ...
assert isinstance(x, count)
assert     hasattr(x, "__next__")
assert not hasattr(x, "__getitem__")
#assert x[0] == 0                    # TypeError: 'itertools.count' object is not indexable
s = 0
for v in x :
    if v == 10 :
        break
    s += v
assert s == 45
for v in x :
    if v == 20 :
        break
    s += v
assert s == 180

x = count(3, 2) # 3, 5, 7, 9, ...
s = 0
for v in x :
    if v > 10 :
        break
    s += v
assert s == 24

print("Done.")
