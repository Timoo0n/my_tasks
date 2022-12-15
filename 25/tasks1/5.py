from fnmatch import *


def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)

def main():
    my_list = []
    count = 0

    for i in range(10**7-1, 1, -1):
        if fnmatch(str(i), '27?7*') and i % 217 == 0:
            r = [j for j in div(i) if j % 2 == 1]
            my_list.append((i, sum(r)))
            count += 1
        if count == 7: break

    for i in sorted(my_list, key=lambda el: el[0]):
        print(*i)

main()
