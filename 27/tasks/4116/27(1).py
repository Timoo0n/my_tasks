with open('27A.txt', 'r', encoding='utf-8') as file:
    n, k = map(int, file.readline().split())
    l = [int(file.readline()) for _ in range(n)]
    st = end = 0
    s = l[0]
    while s+l[end+1] <= k:
        s += l[end + 1]
        end += 1
    value = end
    for i in range(1, n):
        while end+1 != n and l[end+1]-l[i]<= k:
            s += l[end + 1]
            end += 1
        while l[i]-l[st] > k:
            s -= l[st]
            st += 1
        value = max(value, end)
    print(value)
        
