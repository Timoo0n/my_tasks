def div(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}

    return sorted(my_set)


def main():
    for i in range(333_555, 777_999+1):
        r = list(filter(lambda el: len(str(el)) == 2, div(i)))
        if len(r) == 35:
            print(i, min(r), max(r))

        
if __name__ == '__main__': main()
