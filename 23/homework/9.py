def f(c, e):
    if c < e: return 0
    elif c == e: return 1
    return f(c-8, e) + f(c // 2, e)

print(f(102, 43)*f(43, 5))
