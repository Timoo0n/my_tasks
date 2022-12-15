def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def main():
    for i in range(63_000_000, 75_000_001):
        t = i
        while t % 2 == 0: t = t // 2
        if int(t**0.25)**4 == t and p(int(t**0.25)):
            print(i, t)

if __name__ == '__main__':
    main()
