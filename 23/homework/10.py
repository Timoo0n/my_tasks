def f(c, e):
    if c > e or c == 6: return 0
    elif c == e: return 1
    return f(c+2, e) + f(c*3, e)

print(f(1, 25)*f(25, 63))
