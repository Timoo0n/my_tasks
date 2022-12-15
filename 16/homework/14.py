

def f(n):
    d = {i: 0 for i in range(1, n+1)}

    for n in reversed(list(d.keys())):
        if n > 30: d[n] = n**2 + 5 * n + 4
        elif n <= 30 and n % 2 == 0: d[n] = d[n+1] + 3 * d[n+4]
        elif n <= 30 and n % 2 != 0: d[n] = 2 * d[n+2] + d[n+5]
    return d


print(len(list(filter(lambda el: sum(list(map(int, str(el)))) == 27, list(f(1000).values())))))
