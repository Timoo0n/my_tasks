from itertools import *

def f(x, y, z):
    return ((not x) and y and z) or ((not x) and (not z))

table = [(0,0,0),(1,0,0),(1,1,0)]

for p in permutations('xyz'):
    if all(f(**dict(zip(p, row))) for row in table) == 1:
        print(''.join(p))
