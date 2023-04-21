from itertools import *

def f(x,y,z,w): return w and ((z or y) == (z and x))

for p1,p2,p3,p4,p5 in product(range(2),repeat=5):
    table = [
        (1,p1,1,0),
        (0,p2,p3,p4),
        (1,1,1,p5)
        ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,row))) for row in table] == [1,1,0]:
                print(*p, sep='')
