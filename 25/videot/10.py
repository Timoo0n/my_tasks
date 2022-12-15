def div(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def p(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1))


def main():
    num = 650_001

    for i in range(num, num + 1000):
        s = sum(list(filter(lambda el: p(el), div(i))))
        #s = sum([j for j in div(i) if p(j)])
        if s % 100 == 25:
            print(i, s)
        

if __name__ == '__main__': main()
        
        
        
