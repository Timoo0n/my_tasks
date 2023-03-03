from fnmatch import fnmatch

for i in range(0, 10**8, 39):
    if fnmatch(str(i), '12*6789'):
        print(i, i // 39)
