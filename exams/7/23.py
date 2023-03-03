def f(c, e):
    if c > e or c == 43: return 0
    if c == e: return 1
    return f(c+2, e) + f(c+c+1, e) + f(c+c-1, e)
print(f(7, 63))
