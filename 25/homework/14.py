def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)))


def main():
    for i in range(125_697, 125_722):
        l = list(filter(lambda el: p(el), div(i)))
        if len(l) == 2 and l[0]*l[1] == i:
            print(l[0], l[1])
     
                    

main()
