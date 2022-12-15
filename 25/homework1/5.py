from fnmatch import *

def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def f():
    c = 0
    n = 65000

    while c != 7:
        if fnmatch(str(n), '6*97*5?'):
            r = [i for i in div(n) if i % 2 == 0]
            if len(r) >= 4:
                print(n, sum(r)); c += 1
        n += 1


                
