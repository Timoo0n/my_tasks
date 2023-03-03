with open('27_B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [int(file.readline()) for _ in range(n)]
    l *= 2
    l1, s = [], 0
    for i in range(2*n):
        s += l[i]
        l1.append(s)
    s = sum(l[i]*min(i, n-i) for i in range(n))
    mn = s
    number = 1
    for i in range(1, n):
        s = s - (l1[i-1+n//2]-l1[i-1]) + (l1[i+n-1]-l1[i+n//2-1])
        if mn > s or mn == s and number > i+1:
            mn, number = s, i+1
    print(number)
        
