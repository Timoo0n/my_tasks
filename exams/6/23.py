def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+1,e) + f(c*2, e)
print(f(2, 7)*f(7, 16)*f(16, 39))
