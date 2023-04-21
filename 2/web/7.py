from itertools import *

def f(x,y,z,w): return (x == (not y)) <= ((x and w) == z)


for p1,p2,p3,p4,p5 in product(range(2),repeat=5):
    table = [(1,1,p1,p2),
             (1,1,p3,1),
             (p4,1,1,p5)
        ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,row))) for row in table] == [0,0,0]:
                print(''.join(p))
