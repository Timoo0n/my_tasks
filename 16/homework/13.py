

# однострок)
f = lambda n: n + 3 if n <= 18 else ((n // 3) * f(n // 3) + n - 12, f(n-1) + n**2 + 5)[0 if n % 3 == 0 else 1]

print(len(list(filter(lambda el: all(i % 2 == 0 for i in list(map(int, str(el)))), [f(i) for i in range(1, 1001)]))))
