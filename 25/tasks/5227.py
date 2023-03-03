from fnmatch import fnmatch


def div(x):
    s = set()
    for i in range(1, int(x**0.5)):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


for i in range(int(123405**0.5), int(12300405**0.5)+1):
    r = div(i**2)
    if fnmatch(str(i), '3*52?') and len(r) % 2 == 1:
        print(i, max(r - {i}))
        
