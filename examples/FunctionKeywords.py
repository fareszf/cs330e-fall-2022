#!/usr/bin/env python3

# -------------------
# FunctionKeywords.py
# -------------------

print("FunctionKeywords.py")

def f (x, y, z) :
    return [x, y, z]

assert f(2, 3, 4) == [2, 3, 4]
# f(2)                         # TypeError: f() missing 2 required positional arguments: 'y' and 'z'
# f(2, 3, 4, 5)                # TypeError: f() takes 3 positional arguments but 4 were given

assert f(2, z = 4, y = 3) == [2, 3, 4]
# f(z = 4, 2, y = 3)                   # SyntaxError: non-keyword arg after keyword arg
# f(2, x = 2, y = 3)                   # TypeError: f() got multiple values for argument 'x'
# f(2, a = 4, y = 3)                   # TypeError: f() got an unexpected keyword argument 'a'

print("Done.")
