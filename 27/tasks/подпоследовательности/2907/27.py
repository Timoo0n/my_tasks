with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    ms = 0
    k = 0
    s = 0
    l = [float('inf')]*30

    for _ in range(n):
        num = int(file.readline())
        s += num
        
        if num % 2 == 0 and num > 0: k += 1
        if k % 30 == 0: ms = max(ms, s)
        ms = max(ms, s - l[k % 30])

        l[k % 30] = min(s, l[k % 30])
    print(ms)
