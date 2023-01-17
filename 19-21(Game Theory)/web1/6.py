def f(s, c, m, p0, p1):
    if s >= 21: return c%2==m%2
    if c==m: return 0

    l = []
    if p1 != '+1': l += [f(s+1,c+1,m,'+1',p0)]
    if p1 != '+2': l += [f(s+2,c+1,m,'+2',p0)]
    if p1 != '*2': l += [f(s*2,c+1,m,'*2',p0)]

    return any(l) if (c+1)%2==m%2 else all(l)


#p0 ход предыдущего игрока
#p1 наш предыдующий ход
for s in range(1, 21):
    for m in range(1, 6):
        if f(s, 0, m, '', ''):
            print(s, m)
            break
