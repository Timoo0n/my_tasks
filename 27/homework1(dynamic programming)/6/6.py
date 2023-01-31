with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    k1_max = -10**20 # максимальное нечетное
    k0_max = -10**20 # максимальное четное

    for i in range(info):
        num = int(file.readline())

        if num % 2 == 1 and num > k1_max:
            k1_max = num
        elif num % 2 == 0 and num > k0_max:
            k0_max = num

    print(k1_max+k0_max)
