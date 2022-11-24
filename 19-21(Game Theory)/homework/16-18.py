from functools import lru_cache


def moves(t: tuple): return (t[0]+1, t[1]), (t[0], t[1]+1), (t[0]*2, t[1]), (t[0], t[1]*2)


@lru_cache(None)
def f(h: tuple):
    if h[0]*h[1] >= 63: return 'W'
    elif any(f(i) == 'W' for i in moves(h)): return 'P1'
    elif all(f(i) == 'P1' for i in moves(h)): return 'V1'
    elif any(f(i) == 'V1' for i in moves(h)): return 'P2'
    elif all(f(i) == 'P1' or f(i) == 'P2' for i in moves(h)): return 'V2'


def main():
    for i in range(1, 32):
        result = f((2, i))
        if result == 'V2': print(i, result)


if __name__ == '__main__':
    main()