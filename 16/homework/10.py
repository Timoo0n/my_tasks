
def f(n):
    return 1 if n == 1 else f(n-1) - n*g(n-1)


def g(n):
    return 1 if n == 1 else f(n-1) + 2*g(n-1)



#динамическое решение
def f1(n):
    f = {i: 0 for i in range(n+1)}
    g = {i: 0 for i in range(n+1)}
    for n in f.keys():
        if n == 1: f[n] = 1; g[n] = 1
        elif n > 1: f[n] = f[n-1] - n * g[n-1]; g[n] = f[n-1] + 2 * g[n-1]
    return g[n]


print(f1(18)); print(g(18))
