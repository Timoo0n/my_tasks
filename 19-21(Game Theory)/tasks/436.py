from functools import lru_cache


def moves(h):
    a, b = h
    return (a+b, b), (a, a+b)


@lru_cache(None)
def f(h):
    if sum(h) >= 44:
        return 'END'
    elif all(f(i) == 'END' for i in moves(h)):
        return 'П1'
    elif any(f(i) == 'П1' for i in moves(h)):
        return 'В1'
    elif all(f(i) == 'В1' for i in moves(h)):
        return 'П2'
    elif any(f(i) == 'П1' or f(i) == 'П2' for i in moves(h)):
        return 'В2'


def main():
    for i in range(1, 101):
        print(i, f((11, i)))


if __name__ == '__main__':
    main()  # 17
            # 8
            # 34