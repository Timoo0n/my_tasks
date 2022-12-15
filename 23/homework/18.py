

def f(c, e, s):
    if c > e: return 0
    if c == e and s == 7: return 1
    if c == e and s != 7: return 0
    return f(c+1, e, s+1) + f(c+4, e, s+1) + f(c*2, e, s+1)

print(f(3, 27, 0))
