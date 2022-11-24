from functools import lru_cache


def moves(x):
    my_list = []
    if (x+1) <= 72: my_list += [x+1]
    if (x*2) <= 72: my_list += [x*2]
    if (x*3) <= 72: my_list += [x*3]
    return my_list


@lru_cache(None)
def f(h):
    if 43 <= h <= 72: return 'w'
    elif any(f(i) == 'w' for i in moves(h)): return 'p1'
    elif all(f(i) == 'p1' for i in moves(h)): return 'v1'
    elif any(f(i) == 'v1' for i in moves(h)): return 'p2'
    elif all(f(i) == 'p1' or f(i) == 'p2' for i in moves(h)): return 'v2'


def main():
    for i in range(1, 43):
        result = f(i)
        if result == 'v1':
            print(i, result)


if __name__ == '__main__':
    main()