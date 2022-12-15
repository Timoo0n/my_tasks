from fnmatch import *

def f():
    for x in range(0, 10**8, 2023):
        if fnmatch(str(x), '11[02468]??[13579]11'):
            print(x, x // 2023)

def f1():
    for i in range(0, 10**8, 206):
        if fnmatch(str(i), '123*[13579][02468]56'):
            print(i, i // 206)

def f2():
    for j in (1, 3, 5, 7, 9):
        for k in (0, 2, 4, 6, 8):
            n = int(f'123{j}{k}56')
            if n % 206 == 0:
                print(n, n // 206)
                
    for i in range(10):
        for j in (1, 3, 5, 7, 9):
            for k in (0, 2, 4, 6, 8):
                n = int(f'123{i}{j}{k}56')
                if n % 206 == 0:
                    print(n, n // 206)


f2()
