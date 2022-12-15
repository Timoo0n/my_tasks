def f(x, a):
    return (x in list(range(160, 181))) <= ((x % 35 == 0) <= (x % a == 0))


def main():
    for a in range(1, 1000):
        if all(f(x, a) for x in range(1, 10000)):
            print(a)


if __name__ == '__main__': main()
