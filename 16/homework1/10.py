from functools import lru_cache



def f(n):
    l = [0]*n
    for i in range(0, len(l)):
        n = i + 1
        if n < 4: l[i] = 1
        elif n > 3 and n % 2 != 0: l[i] = n
        elif n > 3 and n % 2 == 0: l[i] = l[i-1] + l[i-2] + l[i-3]
    return l


@lru_cache(None)
def f1(n):
    if n < 4: return 1
    elif n > 3 and n % 2 != 0: return n
    elif n > 3 and n % 2 == 0: return f1(n-1)+f1(n-2)+f1(n-3)


def main():
    r = f(2254)
    print(r[2253]-r[2251])


def main1():
    my_dict = dict()
    for i in range(0, 2255):
        my_dict[i] = f1(i)
    print(my_dict[2254]-my_dict[2252])

main1()
