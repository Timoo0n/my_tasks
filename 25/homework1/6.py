from fnmatch import *


def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    my_list = []
    c = 0

    for i in range(10**7, 0, -1):
        if fnmatch(str(i), '9?*55*7'):
            r = sum(div(i)) % 21
            my_list += [(i, r)]
            c += 1
        if c == 5: break

    for i in sorted(my_list, key=lambda el: el[0]):
        print(*i)

main()
