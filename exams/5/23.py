def f(c, e):
    if c == e: return 1
    if c > e: return 0
    return f(c+1, e) + f(c*2, e) + f(c**2, e)

print(f(5, 154))
    
