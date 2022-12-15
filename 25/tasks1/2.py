from fnmatch import *
from itertools import product


def f():
    for i in range(0, 10**9+1, 169):
        if fnmatch(str(i), '345*789?'):
            print(i, i // 169)


def f1():
    for i in product('0123456789', repeat=2):
        for j in range(10):
            i = ''.join(i)
            n = int(f'345{i}789{j}')
            if n % 169 == 0:
                print(n, n // 169)

    for i in range(10):
        for j in range(10):
            n = int(f'345{i}789{j}')
            if n % 169 == 0:
                print(n, n // 169)

    for j in range(10):
            n = int(f'345789{j}')
            if n % 169 == 0:
                print(n, n // 169)
    

f1()
