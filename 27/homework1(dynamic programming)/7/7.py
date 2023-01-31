with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    mv = 10**20
    m31_1 = 10**30
    m31_0 = 10**30

    for _ in range(info):
        num = int(file.readline())

        if num % 31 == 0: mv = min(mv, num*m31_1, num*m31_0)
        else: mv = min(mv, num*m31_1)

        if num % 31 == 0: m31_1 = min(m31_1, num)
        else: m31_0 = min(m31_0, num)

    print(mv)

        
