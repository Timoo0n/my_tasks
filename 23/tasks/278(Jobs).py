def f(currency, end):
    if currency > end:
        return 0
    elif currency == end:
        return 1
    return f(currency+1, end) + f(int(str((int(str(currency)[0])+1))+str(currency)[1]), end)


if __name__ == '__main__':
    print(f(10, 33))