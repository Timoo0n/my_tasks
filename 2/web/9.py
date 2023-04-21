from itertools import *

def f(x,y,z,w): return (x == y) <= (z == w)

count = 0
table = [
    (0,0,0,1),
    (1,1,1,0)
    ]

for p in permutations('xyzw'):
    if any(f(**dict(zip(p, row))) for row in table) == 0:
        count += 1
print(count)
