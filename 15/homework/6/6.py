def f(x, a):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))


def main():
    for a in range(100):
        if all(f(x, a) for x in range(1000)):
            print(a)


if __name__ == '__main__':
    main()