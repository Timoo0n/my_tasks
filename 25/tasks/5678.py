from fnmatch import fnmatch

for i in range(124579, 10**8, 100):
    if fnmatch(str(i), '124*5*79'):
        if i % sum([int(j) for j in str(i) if int(j) % 2 == 1]) == 0:
            print(i, sum(int(j) for j in str(i)))
