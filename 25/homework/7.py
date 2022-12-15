def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    for i in range(1_204_300, 1_204_381):
        s = sum(list(filter(lambda el: el % 2 == 0, div(i))))
        if s != 0 and s % 10 == 0:
            print(i, s)


main()
        
