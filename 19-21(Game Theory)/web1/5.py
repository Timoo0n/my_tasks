def f(s, c, m, p):
    if s >= 43: return c % 2 == m % 2
    if c == m: return 0

    l = []
    if p != '+1': l += [f(s+1, c+1, m, '+1')]
    if p != '+2': l += [f(s+2, c+1, m, '+2')]
    if p != '*2': l += [f(s*2, c+1, m, '*2')]

    return any(l) if (c+1) % 2 == m % 2 else all(l)


for s in range(1, 43):
    for m in range(1, 5):
        if f(s, 0, m, '') == 1:
            print(s, m)
            break
