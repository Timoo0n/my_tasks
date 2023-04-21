from itertools import *

def f(a,b,c,d): return (a <= d) and (not (b <= c))

table = [(1,0,1,0),(1,1,1,0),(0,0,1,0)]

for p in permutations('abcd'):
    if all(f(**dict(zip(p, row))) for row in table) == 1:
        print(''.join(p))
