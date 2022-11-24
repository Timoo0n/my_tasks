from functools import lru_cache


def moves(x):
    return x+1, x*2, x*3


@lru_cache(None)
def f(h):
    if 43 <= h <= 72: return 'w'
    if h > 72: return 'p1'
    elif any(f(i) == 'w' for i in moves(h)): return 'p1'
    elif all(f(i) == 'p1' for i in moves(h)): return 'v1'
    elif any(f(i) == 'v1' for i in moves(h)): return 'p2'
    elif all(f(i) == 'p1' or f(i) == 'p2' for i in moves(h)): return 'v2'


def main():
    for i in range(1, 43):
        result = f(i)
        if result == 'p2': print(i, result)


if __name__ == '__main__':
    main()