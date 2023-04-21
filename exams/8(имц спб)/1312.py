with open('27B_6638.txt') as file:
    n1 = int(file.readline())
    l = []
    s1 = 0
    for _ in range(n1):
        n, k = map(int, file.readline().split())
        k = k // 100 if k % 100 == 0 else k // 100 + 1
        s1 += k
        l.append([n, k, s1])
    s = sum(l[i][1]*(l[i][0]-l[0][0]) for i in range(n1))
    mn = s
    length = 0
    for i in range(1, n1):
        delta = l[i][0]-l[i-1][0]
        s = s + l[i-1][2]*delta - (s1-l[i-1][2])*delta
        if mn > s:
            mn = s
            length = l[i][0]
    print(length)
     
