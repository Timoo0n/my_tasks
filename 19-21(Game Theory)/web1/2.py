def f(s, c, m):
    if s >= 43 and s <= 72: return c % 2 == m % 2
    if s > 72: return c % 2 != m % 2
    if c == m: return 0

    l = [f(s+1, c+1, m), f(s*2, c+1, m), f(s*3, c+1, m)]

    return any(l) if (c+1) % 2 == m % 2 else all(l)


for s in range(1, 43):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 4:
                print(s, m)
            break
