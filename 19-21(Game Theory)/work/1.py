from functools import lru_cache


def moves(a):
    return a+2, a*2


@lru_cache(None)
def f(x):
    if x >= 25: return 'WIN'
    if any(f(i) == 'WIN' for i in moves(x)): return 'П1'
    elif all(f(i) == 'П1' for i in moves(x)): return 'В1'
    elif any(f(i) == 'В1' for i in moves(x)): return 'П2'
    elif all(f(i) == 'П1' or f(i) == 'П2' for i in moves(x)): return 'В2'


if __name__ == '__main__':
    for i in range(1, 30):
        print(i, f(i))