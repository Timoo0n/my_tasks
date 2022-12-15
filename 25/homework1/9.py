from fnmatch import *


n = 700_000
c = 0


while c != 5:
    if not fnmatch(str(n), '*0??3*') and not fnmatch(str(n), '*4??2') and not fnmatch(str(n), '*1*') and n % 13 == 0:
        print(n, sum(list(map(int, str(n))))); c += 1
    if c == 5: break
    n += 1
