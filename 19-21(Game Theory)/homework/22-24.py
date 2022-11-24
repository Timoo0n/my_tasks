from functools import lru_cache


def moves(t: tuple):
    a, b = t
    my_list = []
    if a > 0: my_list += [(a-1, b)]
    if b > 0: my_list += [(a, b-1)]
    if a > 1: my_list += [(a // 2 + a % 2, b)]
    if b > 1: my_list += [(a, b // 2 + b % 2)]
    return my_list


@lru_cache(None)
def f(h: tuple):
    if sum(h) <= 20: return 'W'
    elif any(f(i) == 'W' for i in moves(h)): return 'P1'
    elif all(f(i) == 'P1' for i in moves(h)): return 'V1'
    elif any(f(i) == 'V1' for i in moves(h)): return 'P2'
    elif all(f(i) == 'P1' or f(i) == 'P2' for i in moves(h)): return 'V2'


def main():
    for i in range(11, 50):
        result = f((10, i))
        if result == 'V2': print(i, result)


if __name__ == '__main__':
    main()