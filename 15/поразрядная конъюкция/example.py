def f():
    print(2 & 4)
    print(int(str(int(str(bin(2))[2:]) & int(str(bin(4))[2:])), 2))


if __name__ == '__main__':
    f()