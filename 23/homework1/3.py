def f(c, e, a1, a2, a3):
    if c > e: return 0
    if c == e and (a2+a3) <= 3: return 1
    return f(c+2, e, a1+1, a2, a3) + f(c*3,e, a1, a2+1, a3) + \
           f(c*5, e, a1, a2, a3+1)
print(f(2, 200, 0, 0, 0))
