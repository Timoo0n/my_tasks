def f(a, c, m):
    if a <= 10: return c % 2 == m % 2
    if c == m: return 0

    h = [f(a - 10, c+1, m), f(a // 3, c+1, m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)

c = 0
for a in range(1000):
    for m in range(5):
        if f(a, 0, m):
            if m == 4:
                print(a, m)
                c += 1
            break
print(c)
