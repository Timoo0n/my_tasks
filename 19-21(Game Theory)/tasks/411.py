from functools import lru_cache


def moves(s):
    a, b = s
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)


@lru_cache(None)
def f(s):
    if sum(s) >= 87:
        return 'END'
    elif any(f(x) == 'END' for x in moves(s)):
        return 'П1'
    elif all(f(x) == 'П1' for x in moves(s)):
        return 'В1'
    elif any(f(x) == 'В1' for x in moves(s)):
        return 'П2'
    elif all(f(x) == 'П1' or f(x) == 'П2' for x in moves(s)):
        return 'В2'


def main():
    for i in range(1, 77):
        print(i, f((9, i)))


if __name__ == '__main__':
    main()