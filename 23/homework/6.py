
def f(c, e):
    if c > e: return 0
    elif c == e: return 1
    return f(c+1, e) + f(c*2, e)

print(f(1, 10)*f(10, 20))
