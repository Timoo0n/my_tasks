from fnmatch import *

def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(

for i in range(1, 10**7):
    if fnmatch(str(i), '?6*6*?6') and all(i % j == 0 for j in (6, 7, 8)):
        print(i, sum(div(i)))
        
