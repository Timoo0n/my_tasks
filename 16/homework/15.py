
def f(n):
    if n == 0: return 0
    return f(n // 2 ) if n % 2 == 0 else 1 + f(n - 1)


print(len(list(filter(lambda el: el == 8, [f(i) for i in range(1, 501)]))))
