with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    k = 0
    min_s = float('inf')
    l = [float('-inf')]*n
    s = 0

    for _ in range(n):
        num = int(file.readline())

        s += num
        if num % 3 == 0: k += 1
        if k == 10: min_s = min(min_s, s)
        min_s = min(min_s, s-l[k-10])

        l[k] = max(l[k], s)
    print(min_s)
        
        
