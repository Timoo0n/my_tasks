from fnmatch import *


def f():
    for i in range(0, 10**8+1, 141):
        if fnmatch(str(i), '1234*7'):
            print(i, i // 141)

f()
