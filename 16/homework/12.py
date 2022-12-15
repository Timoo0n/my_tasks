
#пример мемоизации)
cache = {}
def f(n):
    if n == 0: return 1
    elif n == 1: return 3
    if n not in cache:
        cache[n] = f(n-1) - f(n-2) + 3*n; return cache[n]
    return cache[n]

print(f(40))
