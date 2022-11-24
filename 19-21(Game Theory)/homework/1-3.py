from functools import lru_cache


def moves(x): return x+1, x+2, x+3, x*2


@lru_cache(None)
def f(h):
    if h >= 34: return 'WIN'
    elif any(f(i) == 'WIN' for i in moves(h)): return 'П1'
    elif all(f(i) == 'П1' for i in moves(h)): return 'В1'
    elif any(f(i) == 'В1' for i in moves(h)): return 'П2'
    elif all(f(i) == 'П1' or f(i) == 'П2' for i in moves(h)): return 'В2'


def main():
    for i in range(1, 34):
        result = f(i)
        if result == 'В2':
            print(i, result)


if __name__ == '__main__':
    main()
