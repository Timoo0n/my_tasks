with open('27A.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    # сумма
    ms = 0
    # предыдущие числа по критериям
    k_23_0 = 0
    k_23_1 = 0
    k_0 = 0
    k_1 = 0

    for _ in range(info):
        num = int(file.readline())

        if num % 23 == 0 and num % 2 == 0:
            ms = max(num + k_23_0, num + k_0, ms)
        elif num % 23 == 0 and num % 2 == 1:
            ms = max(num + k_23_1, num + k_1, ms)
        elif num %23 != 0 and num % 2 == 0:
            ms = max(ms, num + k_23_0)
        elif num % 23 != 0 and num % 2 == 1:
            ms = max(ms, num + k_23_1)

        if num % 23 == 0 and num % 2 == 0: k_23_0 = max(k_23_0, num)
        elif num % 23 == 0 and num % 2 == 1: k_23_1 = max(k_23_1, num)
        elif num % 23 != 0 and num % 2 == 0: k_0 = max(k_0, num)
        elif num % 23 != 0 and num % 2 == 1: k_1 = max(k_1, num)

    print(ms)
