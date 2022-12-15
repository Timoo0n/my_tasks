def f(c, e):
    if c > e or c in (11, 18): return 0
    if c == e: return 1
    if c < e: return f(c+1, e) + f(c+2, e) + f(c*3, e)


def f1():
    l = [0]*100
    l[4] = 1
    for i in range(4, 8):
        #l[11] = 0; l[18] = 0
        if i + 1 <= 8: l[i+1] += l[i]
        if i + 2 <= 8: l[i+2] += l[i]
        if i * 3 <= 8: l[i*3] += l[i]
    for i in range(8, 23):
        l[11] = 0; l[18] = 0
        if i + 1 <= 23: l[i+1] += l[i]
        if i + 2 <= 23: l[i+2] += l[i]
        if i * 3 <= 23: l[i*3] += l[i]
    return l[23]


print(f(4, 8)*f(8, 23))
     
