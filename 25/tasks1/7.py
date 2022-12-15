from fnmatch import *
for i in range(121*50_000, 10**10, 121):
    if fnmatch(hex(i)[2:], '1?ded?ced'):
        print(i, i // 121)
