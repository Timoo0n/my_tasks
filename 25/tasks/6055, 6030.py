from fnmatch import fnmatch


def task6055():
    for i in range(0, 10**7, 159):
        if fnmatch(str(i), '2?1*67'): print(i, i // 159)


def task6030():
    for i in range(0, 10**8, 129):
        if fnmatch(str(i), '12?3*46'): print(i, i // 129)

task6030()
        
