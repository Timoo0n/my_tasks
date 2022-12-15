def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+1, e) + f(c*2, e) + f(c*2+1, e) + f(c*10, e)

print(f(1, 15))
