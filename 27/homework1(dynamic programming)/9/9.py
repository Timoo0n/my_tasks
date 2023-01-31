with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    q = [int(file.readline()) for i in range(8)]
    k = k23 = count = 0

    for _ in range(info - 8):
        n = int(file.readline())
        if n % 23 == 0: count += k
        else: count += k23

        k += 1
        if  q[0] % 23 == 0: k23 += 1
        q.append(n)
        q.pop(0)
    print(count)
        

        
