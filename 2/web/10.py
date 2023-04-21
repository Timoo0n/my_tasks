from itertools import *

def f(x,y,z,w): return x and (y <= z) or w
s = set()

for p1,p2,p3,p4,p5,p6 in product(range(2),repeat=6):
    table = [
        (1,0,p1,1),
        (p2,0,1,p3),
        (p4,0,p5,p6)
        ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if not any(f(**dict(zip(p, row))) for row in table):
                s.add(p)
print(len(s))
