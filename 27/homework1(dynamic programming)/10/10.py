with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    q = [int(file.readline()) for i in range(4)]

    k13_1 = k13_0 = k0 = k1 = count = 0

    for _ in range(info-4):
        num = int(file.readline())

        if num % 13 == 0 and num % 2 == 0: count += k1 
        elif num % 13 == 0 and num % 2 == 1: count += k0
        elif num % 13 != 0 and num % 2 == 0: count += k13_1
        elif num % 13 != 0 and num % 2 == 1: count += k13_0

        if q[0] % 2 == 0: k0 += 1
        elif q[0] % 2 == 1: k1 += 1

        if q[0] % 13 == 0 and q[0] % 2 == 1: k13_1 += 1
        elif q[0] % 13 == 0 and q[0] % 2 == 0: k13_0 += 1
        q.pop(0)
        q.append(num)
    print(count)
    
