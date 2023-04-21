with open('27_6529b.txt', 'r', encoding='utf-8') as file:
    n, m = map(int, file.readline().split())

    l = [int(file.readline()) for _ in range(n)]
    length = float('-inf')

    l1 = [0]*(n+1)
    for i in range(1, n+1):
        l1[i] = l1[i-1]+l[i-1]

    end = 0
    for i in range(n):
        st = i
        while end < n and l1[end+1] - l1[st] <= m:
            end += 1
        length = max(length, end-st)
    print(length)
        
    
        
