from functools import lru_cache

def moves(x):
    return x+1, x+4, x*2


@lru_cache(None)
def f(h):
    if h >= 165: return 'w'
    elif any(f(i) == 'w' for i in moves(h)): return 'p1'
    elif all(f(i) == 'p1' for i in moves(h)): return 'v1'
    elif any(f(i) == 'v1' for i in moves(h)): return 'p2'
    elif any(f(i) == 'p1' or f(i) == 'p2' for i in moves(h)): return 'v2'


def main():
    for i in range(1, 165):
        result = f(i)
        if result == 'v2': print(i)


if __name__ == '__main__': main()
