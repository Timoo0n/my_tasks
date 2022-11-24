from functools import lru_cache


def moves(x):
    return [x // 2 if x % 2 == 0 else x - 2, x // 3 if x % 3 == 0 else x - 3]


@lru_cache(None)
def f(h):
    if h == 1: return 'WIN'
    elif any(f(i) == 'WIN' for i in moves(h)): return 'П1'
    elif all(f(i) == 'П1' for i in moves(h)): return 'В1'
    elif any(f(i) == 'В1' for i in moves(h)): return 'П2'
    elif all(f(i) == 'П1' or f(i) == 'П2' for i in moves(h)) and any(f(i) == 'П1' for i in moves(h)): return 'В2'


def main():
    for i in range(2, 38):
        result = f(i)
        if result == 'В2':
            print(i, result)


if __name__ == '__main__':
    main()

# 5
# 7 18
#