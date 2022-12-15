from functools import *
from sys import *

setrecursionlimit(10**8)


@lru_cache(None)
def f(c, e, s):
    if c > e: return 0
    elif c == e and s == 8: return 1
    elif c == e and s != 8: return 0
    return f(c+1, e, s+1) + f(c+5, e, s+1) + f(c*3, e, s+1)

c = 0
for i in range(1000, 1025):
    r = f(1, i, 0)
    if r != 0:
        c += 1

print(c)
