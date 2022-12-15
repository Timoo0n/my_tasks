from fnmatch import *


def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


my_list = list()
c = 0

for i in range(10**7, 1, -1):
    if fnmatch(str(i), '14?4*') and i % 217 == 0:
        my_list += [(i, sum([j for j in div(i) if j % 2 != 0]))]
        c += 1
    if c == 7: break

for i in sorted(my_list, key=lambda el: el[0]):
    print(*i)
