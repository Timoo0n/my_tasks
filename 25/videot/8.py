
def div(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}

    return sorted(my_set)


def main():
    num = 500_001
    count = 0

    while count != 5:
        result = list(filter(lambda el: el != 8 and el % 10 == 8, div(num)))
        if len(result) != 0:
            print(num, min(result))
            count += 1
        num += 1


if __name__ == '__main__': main()
            
        
    
