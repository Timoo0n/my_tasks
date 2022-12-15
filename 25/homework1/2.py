from fnmatch import *


def f():
    for i in range(10):
        n = int(f'123567{i}')
        if n % 169 == 0:
            print(n, n // 169)

        
    for i in range(0, 10**9, 169):
        if fnmatch(str(i), '123*567?'):
            print(i, i // 169)

f()
