from itertools import *

def f(x,y,z,w): return ((x <= z) <= y) or (not w)

for p1,p2,p3,p4,p5,p6,p7 in product(range(2),repeat=7):
    table = [(1,0,p1,p2),
             (p3,1,0,p4),
             (0,p5,p6,p7)
             ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in table] == [0,0,0]:
                print(''.join(p))
