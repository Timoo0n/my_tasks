def f(x, a):
    return (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))


def main():
    for a in range(1000):
        if all(f(x, a) for x in range(10000)):
            print(a)


if __name__ == '__main__':
    main()