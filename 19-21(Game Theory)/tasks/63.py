from functools import lru_cache


def moves(s):
    a, b = s
    return (a+b, b), (a, a+b)


@lru_cache(None)
def f(s):
    if sum(s) >= 80:
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
    for s in range(1, 100):
        print(s, f((20, s)))
    

if __name__ == '__main__':
    main()