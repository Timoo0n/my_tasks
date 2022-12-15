from fnmatch import *

def f():
    for i in range(0, 10**6, 51):
        if fnmatch(str(i), '56*98*'):
            print(i, i // 51)


def f1():
    for i in range(1020, 10**6+1, 51):
        n = str(i)
        if n[:2] == '56' and '98' in n[2:] and i % 51 == 0:
            print(i, i // 51)

f1(); f()
            
