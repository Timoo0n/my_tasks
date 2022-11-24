from functools import lru_cache


def moves(a):
    x, y = a
    return (x+1, y), (x, y+1), (x*2, y), (x, y*2)


@lru_cache(None)
def f(h):
    if sum(h) >= 40: return 'WIN'
    elif any(f(i) == 'WIN' for i in moves(h)): return 'П1'
    elif all(f(i) == 'П1' for i in moves(h)): return 'В1'
    elif any(f(i) == 'В1' for i in moves(h)): return 'П2'
    elif all(f(i) == 'П1' or f(i) == 'П2' for i in moves(h)): return 'В2'


if __name__ == '__main__':
    for i in range(1, 32):
        print(i, f((9, i)))
