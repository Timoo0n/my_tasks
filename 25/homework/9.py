def div(x: int) -> list:
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    n = 300_001
    c = 0
    while c != 5:
        r = list(filter(lambda el: el % 3 == 0, div(n)))
        if len(r) == 5:
            print(n, max(r)); c += 1
        n += 1


main()
    
