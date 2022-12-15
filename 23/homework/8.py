
def f(c, e):
    if c > e: return 0
    elif c == e: return 1
    return f(c+1, e) + f(c+3, e) + f(c*2, e)

print(f(3, 9)*f(9, 12)*f(12, 20))
