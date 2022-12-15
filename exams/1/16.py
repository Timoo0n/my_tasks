from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10**9)


@lru_cache(None)
def f(n):
    if n >= 10_000: return n
    elif (n < 10_000) and (n % 2 == 0): return f(n+2) - 3
    elif (n < 10_000) and (n % 2 == 1): return f(n+2) + 1


def main():
    my_dict = dict()
    for i in range(10000, 2, -1):
        my_dict[i] = f(i)
    print(my_dict[94]-my_dict[80])


if __name__ == '__main__': main()
    
