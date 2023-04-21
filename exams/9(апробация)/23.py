def f(c, e):
    if c <= e: return c == e
    return f(c-2, e) + f(c//2, e)
print(f(40,10)*f(10,2))
