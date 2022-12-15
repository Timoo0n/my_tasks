

def f(n):
    if n <= 3: return n
    elif n > 3 and n % 3 == 0: return n**3 + f(n - 1)
    elif n > 3 and n % 3 == 1: return 4 + f(n // 3)
    return n**2 + f(n - 2)



#динамическое решение
def f1(n):
    l = {i: 0 for i in range(n+1)}
    for n in l.keys():
        if n <= 3: l[n] = n
        elif n > 3 and n % 3 == 0: l[n] = n**3 + l[n-1]
        elif n > 3 and n % 3 == 1: l[n] = 4 + l[n // 3]
        elif n > 3 and n % 3 == 2: l[n] = n**2 + l[n-2]
    return l[n]


print(f1(100)); print(f(100))
