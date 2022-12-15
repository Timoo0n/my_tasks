from fnmatch import *

count = n = 0

def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)
    

while count != 7:
    if fnmatch(str(n), '?8*8*?8') and all(n % i == 0 for i in (6, 7, 8)):
        print(n, sum(div(n))); count += 1
    n += 1
