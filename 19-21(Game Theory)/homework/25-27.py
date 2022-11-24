from functools import lru_cache


def moves(t): return t*3, t+1


@lru_cache(None)
def f(h):
    if h >= 2163: return 'W'
    elif any(f(i) == 'W' for i in moves(h)): return 'P1'
    elif all(f(i) == 'P1' for i in moves(h)): return 'V1'
    elif any(f(i) == 'V1' for i in moves(h)): return 'P2'
    elif all(f(i) == 'P1' or f(i) == 'P2' for i in moves(h)): return 'V2'


def main():
    for i in range(2163, 1, -1):
        result = f(i)
        if result == 'V2':
            print(i, f(i))


if __name__ == '__main__':
    main()