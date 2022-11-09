#!/usr/bin/env python3

# --------------
# NaturalJoin.py
# --------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

from ThetaJoin import theta_join_generator

def natural_join_yield (r, s) :
    def bp (u, v) :
        return not any(u[k] != v[k] for k in u if k in v)
    for u in r :
        for v in s :
            if bp(u, v) :
                yield dict(u, **v)

def natural_join_generator (r, s) :
    def bp (u, v) :
        return not any(u[k] != v[k] for k in u if k in v)
    return (dict(u, **v) for u in r for v in s if bp(u, v))

def natural_join_theta_join (r, s) :
    def bp (u, v) :
        return not any(u[k] != v[k] for k in u if k in v)
    return theta_join_generator(r, s, bp)
