from functools import lru_cache


def moves(x): return x+1, x*2, x*3


@lru_cache(None)
def f(h):
    if 36 <= h <= 60: return 'WIN'
    elif h > 60: return 'P1'
    elif any(f(i) == 'WIN' for i in moves(h)): return 'P1'
    elif all(f(i) == 'P1' for i in moves(h)): return 'V1'
    elif any(f(i) == 'V1' for i in moves(h)): return 'P2'
    elif all(f(i) == 'P1' or f(i) == 'P2' for i in moves(h)): return 'V2'


def main():
    for i in range(1, 36):
        result = f(i)
        if result == 'V2':
            print(i, result)


if __name__ == '__main__':
    main()