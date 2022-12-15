def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    c = 0
    l = []
    for i in range(22360, 10000, -1):
        r = div(i**2)
        if len(r) == 7: l.append((i**2, max(r))); c += 1
        if c == 5: break
    l = sorted(l, key=lambda el: el[0])
    for i in l:
        print(*i)


main()
