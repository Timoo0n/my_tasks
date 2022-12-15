from functools import lru_cache


@lru_cache(None)
def f(n):
    return f(n-1) - 2*g(n-1) if n > 1 else 1


@lru_cache(None)
def g(n):
    return f(n-1)+g(n-1)+n if n > 1 else 1


print(sum(list(map(int, str(g(36))))))
