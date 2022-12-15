from fnmatch import *

def f():
    for x in range(0, 10**9, 17):
        if fnmatch(str(x), f'23?456?89'):
            print(x, x // 17)


def f1():
    for i in range(10):
        for j in range(10):
            n = int(f'23{i}456{j}89')
            if n % 17 == 0:
                print(n, n // 17)

f1()
f()
