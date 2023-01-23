def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def main():
    c = 0
    for i in range(113000000, 114000001):
        if i % 2 == 0 and i % 4 != 0:
            t = i // 2
            if int(t**0.5)**2 == t and p(int(t**0.5)):
                print(i, 2*int(t**0.5))
        

main()
