def f(s, m):
    if s >= 166: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+2,m-1), f(s+10,m-1)] + [f(s + s*i, m-1) for i in range(1,100) if s*i <= 80]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 166) if f(s, 3)])  # all -> any Ответ: 1
#print('20)', [s for s in range(1, 166) if not f(s, 1) and f(s, 3)])  # Ответ: 77 153
#print('21)', [s for s in range(1, 166) if not f(s, 2) and f(s, 4)])  # 142
