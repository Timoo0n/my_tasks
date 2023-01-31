with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    q = [int(file.readline()) for _ in range(5)]
    k1 = k3 = k9 = k7 = count = 0

    for _ in range(info-5):
        n = int(file.readline())

        if n % 10 == 9: count += k7
        elif n % 10 == 7: count += k9
        elif n % 10 == 3: count += k1
        elif n % 10 == 1: count += k3

        value = q[0]
        if value % 10 == 9: k9 += 1
        elif value % 10 == 3: k3 += 1
        elif value % 10 == 1: k1 += 1
        elif value % 10 == 7: k7 += 1

        q.pop(0)
        q.append(n)
    print(count)

        

    
