with open('27-B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    k0 = []  # четные
    k1 = []  # нечетные
    count = 0

    for _ in range(n):
        num = int(file.readline())

        if num % 2 == 0:
            if k1 and num > min(k1):
                count += len(k1)
        else:
            if k0 and num > min(k0):
                count += len(k0)

        if num % 2 == 0:
            k0 += [num]
        else:
            k1 += [num]
    print(count)
