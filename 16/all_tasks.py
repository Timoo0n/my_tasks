from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1: return 2
    elif n > 1: return f(n-1) + 5 * n**2


    
def f1(n):
    l = [0]*n
    for i in range(len(l)):
        n = i + 1
        if n == 1: l[i] = 2
        elif n > 1: l[i] = l[i-1] + 5 * n**2
    return l[n-1]

@lru_cache(None)
def f_1(n):
    if n < 3: return n + 3
    elif n >= 3 and n % 3 == 0: return (n+2)*f_1(n-4)
    elif n >= 3 and n % 3 != 0: return n + f_1(n-1)+2*f_1(n-2)

def f1_1(n):
    l = {i: 0 for i in range(-1, n+1)}
    for n in l.keys():
        if n < 3: l[n] = n + 3
        elif n >= 3 and n % 3 == 0: l[n] = (n + 2) * l[n-4]
        elif n >= 3 and n % 3 != 0: l[n] = n + l[n-1] + 2 * l[n-2]
    return l[n]

@lru_cache(None)
def f_2(n):
    if n == 1: return 1
    elif n > 1: return 2 * f_2(n - 1) + g_2(n - 1) - 2


@lru_cache(None)
def g_2(n):
    if n == 1: return 1
    elif n > 1: return f_2(n - 1) + 2 * g_2(n - 1)


@lru_cache(None)
def f_3(n):
    k = 0
    k += 1
    if n >= 1:
        k += 1
        k += f_3(n-1)
        k += f_3(n-3)
        k += 1
    return k

@lru_cache(None)
def f_4(n):
    s = 0
    s += n+1
    if n > 1:
        s += n + 5 + f_4(n-1) + f_4(n-2)
    return s

def f_5(n):
    g = [0] * n
    f = [0] * n
    for i in range(n):
        n = i + 1
        if n == 1: g[i] = 1; f[i] = 1
        elif n > 1: f[i] = f[i-1] + 3 * g[i-1]; g[i] = f[i-1] - 2*g[i-1]
    return f[n-1]

@lru_cache(None)
def f1_5(n):
    return 1 if n == 1 else f1_5(n-1)+3*g1_5(n-1)

@lru_cache(None)
def g1_5(n):
    return 1 if n == 1 else f1_5(n-1) - 2*g1_5(n-1)


@lru_cache(None)
def f_6(n):
    if n < -100_000: return 1
    elif n > 10: return f_6(n-1)+3*f_6(n-3)+2
    else: return -f_6(n-1)

def main_6():
    my_dict = dict()
    for i in range(-100_001, 21):
        my_dict[i] = f_6(i)
    print(my_dict[20])

main_6()
        
