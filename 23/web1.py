from functools import lru_cache

@lru_cache(None)
def f(c, e):
    if c > e: return 0
    elif c == e: return 1
    return f(int(bin(c + 1)[2:], 2), e) + f(int(bin(c)[2:]+'1', 2), e) + f(int(bin(c)[2:]+'0', 2), e)

print(f(4, 218))   
