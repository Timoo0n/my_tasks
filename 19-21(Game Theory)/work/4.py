from functools import lru_cache


def moves(h):
    a, b = h
    return (4*a, b), (a, 4*b), (a+1, b), (a, b+1)


@lru_cache(None)
def f(h: tuple):
    if h[0]*h[1] >= 1056: return 'WIN'
    if any(f(i) == 'WIN' for i in moves(h)): return 'П1'
    if all(f(i) == 'П1' for i in moves(h)): return 'В1'
    if any(f(i) == 'В1' for i in moves(h)): return 'П2'
    if all(f(i) == 'П1' or f(i) == 'П2' for i in moves(h)): return 'В2'


if __name__ == '__main__':
    for i in range(1, 132):
        result = f((8, i))
        if result == 'В2':
            print(i, result)
