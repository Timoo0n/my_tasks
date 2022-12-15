from functools import lru_cache



@lru_cache(None)
def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+2, e) + f(c+4, e) + f(c+5, e)


print(f(31, 56))
