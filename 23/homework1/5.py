def f(c, e, count):
    if c > e: return 0
    if c == e and count == 6: return 1

    return f(c+1, e, count + (1, 0)[(c+1) % 2])\
           + f(c+3, e, count + (1, 0)[(c+3) % 2])\
           + f(c+5, e, count + (1, 0)[(c+5) % 2])

print(f(3, 25, 0))
