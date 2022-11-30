#!/usr/bin/env python3

# --------
# StdDev.py
# --------

from functools  import reduce
from math       import sqrt
from numpy      import std
from statistics import mean, StatisticsError

def stdev_range_for (a) :
    if len(a) < 2 :
        raise StatisticsError("variance requires at least two data points")
    m = mean(a)
    v = 0
    for i in range(len(a)) :
        v += (a[i] - m) ** 2
    return sqrt(v / (len(a) - 1))

def stdev_for (a) :
    if len(a) < 2 :
        raise StatisticsError("variance requires at least two data points")
    m = mean(a)
    v = 0
    for u in a :
        v += (u - m) ** 2
    return sqrt(v / (len(a) - 1))

def stdev_reduce (a) :
    if len(a) < 2 :
        raise StatisticsError("variance requires at least two data points")
    m = mean(a)
    v = reduce(lambda w, u : w + (u - m) ** 2, a, 0)
    return sqrt(v / (len(a) - 1))

def stdev_map (a) :
    if len(a) < 2 :
        raise StatisticsError("variance requires at least two data points")
    m = mean(a)
    v = sum(map(lambda v : (v - m) ** 2, a))
    return sqrt(v / (len(a) - 1))

def stdev_list (a) :
    if len(a) < 2 :
        raise StatisticsError("variance requires at least two data points")
    m = mean(a)
    v = sum([(v - m) ** 2 for v in a])
    return sqrt(v / (len(a) - 1))

def stdev_generator (a) :
    if len(a) < 2 :
        raise StatisticsError("variance requires at least two data points")
    m = mean(a)
    v = sum((v - m) ** 2 for v in a)
    return sqrt(v / (len(a) - 1))

def stdev_numpy (a) :
    if len(a) < 2 :
        raise StatisticsError("variance requires at least two data points")
    return std(a, ddof = 1)