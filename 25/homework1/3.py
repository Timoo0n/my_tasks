from fnmatch import *


def f():
    for i in range(0, 10**6+1, 51):
        if fnmatch(str(i), '12*45*'):
            print(i, i // 51)

f()
