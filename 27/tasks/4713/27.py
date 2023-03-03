with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = []
    s = 0
    for _ in range(n):
        km, num = map(int, file.readline().split())
        num = num // 36 if num % 36 == 0 else num // 36 + 1
        s += num
        l.append([km, num, s])
    sm = s
    s = 0
    for i in range(n):
        s += abs(l[i][0]-l[0][0])*l[i][1]
    mn = s
    for i in range(1, n):
        r = abs(l[i][0]-l[i-1][0])
        s = s + l[i-1][2]*r - (sm - l[i-1][2])*r
        mn = min(mn, s)
    print(mn)
