from functools import lru_cache


def moves(h: tuple): return (h[0]+3, h[1], h[2]), (h[0], h[1]+3, h[2]), (h[0], h[1], h[2]+3), \
                            (h[0]+13, h[1], h[2]), (h[0], h[1]+13, h[2]), (h[0], h[1], h[2]+13), \
                            (h[0]+23, h[1], h[2]), (h[0], h[1]+23, h[2]), (h[0], h[1], h[2]+23)


@lru_cache(None)
def f(t: tuple):
    if sum(t) >= 73: return 'W'
    elif any(f(i) == 'W' for i in moves(t)): return 'P1'
    elif all(f(i) == 'P1' for i in moves(t)): return 'V1'
    elif any(f(i) == 'V1' for i in moves(t)): return 'P2'
    elif all(f(i) == 'P1' or f(i) == 'P2' for i in moves(t)): return 'V2'


def main():
    for i in range(1, 24):
        result = f((2, i, i*2))
        if result == 'V2': print(i, result)


if __name__ == '__main__':
    main()