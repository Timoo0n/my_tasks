def f(currency, end):
    if currency > end or currency == 6:
        return 0
    elif currency == end:
        return 1

    return f(currency+2, end) + f(currency*3, end)


if __name__ == '__main__':
    print(f(1, 25) * f(25, 63))