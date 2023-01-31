with open('test.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    q = [int(file.readline()) for i in range(5)]
    count = 0

    m13_1 = [0]*13 #  четные остатки
    m13_0 = [0]*13 #  нечетные остатки
    for i in range(info-5):
        num = int(file.readline())
        if num % 2 == 0: count += (m13_1[num % 13] + m13_0[num % 13])
        else: count += m13_1[num % 13]

        value = q.pop(0)
        if value % 2 == 0: m13_1[value % 13] += 1
        elif value % 2 == 1: m13_0[value % 13] += 1

        q.append(num)

    print(count)
