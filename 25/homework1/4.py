from fnmatch import *


def f():
    for i in range(10):
        n = int(f'1{i}21394')
        if n % 2023 == 0:
            print(n, n // 2023)

    for i in range(0, 10**10, 2023):
        if fnmatch(str(i), '1?2139*4'):
            print(i, i // 2023)

f()
