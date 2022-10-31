def f(currency, end):
    if currency > end:
        return 0
    elif currency == end:
        return 1
    return f(currency+1, end) + f(currency+3, end) + f(currency*2, end)


if __name__ == '__main__':
    print(f(1, 15))