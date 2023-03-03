def f(c, e, a1, a2, a3):
    if c > e: return 0
    if c == e and a3 == 1: return 1
    return f(c+1, e, a1+1, a2, a3) + f(c+2, e, a1, a2+1, a3)\
           + f(c*2, e, a1, a2, a3+1)
print(f(2, 12, 0, 0, 0))
