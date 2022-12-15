num = 1_500_001
count = 0

while count != 6:
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}

    if len(my_set) != 0:
        f = int(sum(my_set)/len(my_set))
        if f % 10 == 9:
            print(num, f)
            count += 1
    num += 1
