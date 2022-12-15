def f(x, a):
    return ((x % 6 == 0) <= (not (x % 10 == 0))) or (x + a > 121)


def main():
    for a in range(1, 200):
        if all(f(x, a) for x in range(10000)):
            print(a)


if __name__ == '__main__': main()
