from functools import lru_cache


def moves(x: tuple): return (x[0]+1, x[1]), (x[0], x[1]+1), (x[0]*2, x[1]), (x[0], x[1]*2)


@lru_cache(None)
def f(h: tuple):
    if sum(h) >= 59: return 'WIN'
    elif any(f(i) == 'WIN' for i in moves(h)): return 'P1'
    elif all(f(i) == 'P1' for i in moves(h)): return 'V1'
    elif any(f(i) == 'V1' for i in moves(h)): return 'P2'
    elif all(f(i) == 'P1' or f(i) == 'P2' for i in moves(h)): return 'V2'


def main():
    for i in range(2, 53):
        result = f((5, i))
        if result == 'V2': print(i, result)


if __name__ == '__main__':
    main()