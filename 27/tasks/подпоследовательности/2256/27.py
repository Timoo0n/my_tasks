with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    s = 0
    ms = 0
    
    l = [float('inf')]*3
    k5 = 0
    for _ in range(n):
        num = int(file.readline())
        s += num
        if num % 5 == 0: k5 += 1
        if k5 % 3 == 0: ms = max(s, ms)
        ms = max(ms, s-l[k5%3])

        l[k5 % 3] = min(l[k5 % 3], s)
    print(ms)
