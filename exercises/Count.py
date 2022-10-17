#!/usr/bin/env python3

# ------
# Count.py
# ------

# count(start, [step])
# ------------------------------
# Count starts counting up from a provided starting argument,
# optionally steps by provided step

def count_while(start, *step):
    if not step :
       s = 1
    else :
       s = step[0]
    n = start
    while True:
        yield n
        n += s