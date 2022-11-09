#!/usr/bin/env python3

# ------------
# ThetaJoin.py
# ------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

def theta_join_yield (r, s, bp) :
    for u in r :
        for v in s :
            if bp(u, v) :
                yield dict(u, **v)

def theta_join_generator (r, s, bp) :
    return (dict(u, **v) for u in r for v in s if bp(u, v))
