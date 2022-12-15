def f(currency, end):
    if currency > end: return 0
    elif currency == end: return 1
    return f(currency+3, end) + f(currency*2, end)


def main():
    print(f(3, 27)*f(27, 63))


if __name__ == '__main__': main()
