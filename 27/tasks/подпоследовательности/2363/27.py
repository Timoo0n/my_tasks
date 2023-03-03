with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    q = []
    s = 0
    count = 0
    for _ in range(4):
        num = int(file.readline())
        q += [num]
        s += num

    l = [0]*117
    
    for _ in range(n-4):
        num = int(file.readline())
        s += num
        if s % 117 == 0: count += 1
        count += l[s % 117]

        s1 = q.pop(0)
        l[s1 % 117] += 1
        q.append(s)
    print(count)
