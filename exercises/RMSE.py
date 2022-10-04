#!/usr/bin/env python3

#pylint: disable = bad-builtin, consider-using-enumerate, no-name-in-module

# -------
# RMSE.py
# -------

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.square.html
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.subtract.html

from functools import reduce
from math      import sqrt
from numpy     import mean, sqrt, square, subtract

def rmse_range_for (a, p) :
    v = 0
    for i in range(len(a)) :
        v += (a[i] - p[i]) ** 2
    return sqrt(v / len(a))

def rmse_zip_for (a, p) :
    z = zip(a, p)
    v = 0
    for x, y in z :
        v += (x - y) ** 2
    return sqrt(v / len(a))

def rmse_zip_reduce (a, p) :
    z = zip(a, p)
    v = reduce(lambda u, w : u + (w[0] - w[1]) ** 2, z, 0)
    return sqrt(v / len(a))

def rmse_zip_map_sum (a, p) :
    z = zip(a, p)
    v = sum(map(lambda u : (u[0] - u[1]) ** 2, z))
    return sqrt(v / len(a))

def rmse_zip_list_sum (a, p) :
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z])
    return sqrt(v / len(a))

def rmse_zip_generator_sum (a, p) :
    z = zip(a, p)
    v = sum((x - y) ** 2 for x, y in z)
    return sqrt(v / len(a))

def rmse_map_sum (a, p) :
    v = sum(map(lambda x, y : (x - y) ** 2, a, p))
    return sqrt(v / len(a))

def rmse_numpy (a, p) :
    return sqrt(mean(square(subtract(a, p))))
