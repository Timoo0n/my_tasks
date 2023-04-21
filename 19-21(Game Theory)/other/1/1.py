def f(s, m):
    if s >= 82: return m % 2 != 0
    if m == 0: return 0
    h = [f(s+10, m-1), f(s*2, m-1)]
    return any(h) if m%2 != 0 else all(h)

print('19)', [s for s in range(1, 82) if not f(s, 1) and f(s,3)])
print('20)', [s for s in range(1, 82) if not f(s, 2) and f(s, 4)])
print('20)', [s for s in range(1, 82) if not f(s, 3) and f(s, 5)])
