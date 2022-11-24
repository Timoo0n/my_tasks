from functools import lru_cache


def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a+b, b), (a, b+a)


@lru_cache(None)
def f(x):
    if sum(x) >= 81: return 'WIN'
    elif any(f(i) == 'WIN' for i in moves(x)): return 'П1'
    elif all(f(i) == 'П1' for i in moves(x)): return 'В1'
    elif any(f(i) == 'В1' for i in moves(x)): return 'П2'
    elif all(f(i) == 'П1' or f(i) == 'П2' for i in moves(x)): return 'В2'


if __name__ == '__main__':
    for i in range(1, 74):
        result = f((7, i))
        if result == 'В2':
            print(i, result)

# 23
# 22 36
# 35