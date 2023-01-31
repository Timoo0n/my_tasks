from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return f(n-1) + n * f(n-1)

for i in range(10_000): f(i)

print(f(5997)/f(5995))
