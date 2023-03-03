def div(x):
    s = set()
    for i in range(2, int(x**0.5)):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)

for i in range(135790, 163228+1):
    r = div(i)
    if sum(r) > 460000:
        print(len(r), sum(r))
