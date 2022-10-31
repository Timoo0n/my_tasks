def f():
    print('X Y Z W')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not ((((not y) <= w) <= (x <= z)) <= (x <= w)):
                        print(x, y, z, w)


def main():
    f()


if __name__ == '__main__':
    main()