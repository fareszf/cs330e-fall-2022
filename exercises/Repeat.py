from itertools import repeat

# ------
# Repeat.py
# ------

# repeat(elem, [n]): Repeat will repeat an item endlessly or up to n (optional) times
def repeat_while(s, *a) :
    if a :      
       x = 0
       while (x < a[0]) :
          yield s
          x += 1
    else :    
       while True :
          yield s