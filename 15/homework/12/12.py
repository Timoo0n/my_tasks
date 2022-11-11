def f(x, y, a):
    return ((2*x+y) != 70) or (x < y) or (a < x)


def main():
    for a in range(1, 1000):
        if all(f(x, y, a) for x in range(100) for y in range(100)):
            print(a)


if __name__ == '__main__':
    main()