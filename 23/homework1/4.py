from functools import lru_cache

@lru_cache(None)
def f(c, e, count):
    if c > e: return 0
    if c == e and count == 1: return 1
    return f(c+1, e, count + ((c+1) % 2)) + f(c+2, e, count + ((c+2) % 2)) \
           + f(c*2, e, count + ((c*2) % 2))

print(f(2, 40, 0))
