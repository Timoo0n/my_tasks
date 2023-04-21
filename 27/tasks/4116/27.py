with open('27B.txt', 'r', encoding='utf-8') as file:
    n, k = map(int, file.readline().split())
    l = [int(file.readline()) for _ in range(n)]
    l1 = [0]*(n+1)
    for i in range(1, n+1):
        l1[i] = l1[i-1]+l[i-1]

    end, length  = 0, float('-inf')
    for st in range(n):
        while end < n and l1[end+1]-l1[st] <= k: end += 1
        length = max(length, end-st)
    print(length)
