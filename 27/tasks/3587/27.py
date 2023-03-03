with open('27_B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [int(file.readline()) for _ in range(n)]
    value = sum(l)
    s = 0
    for i in range(n):
        s += l[i] * min(i, n-i)
    l *= 2

    l1 = []
    s1 = 0
    for i in range(2*n):
        s1 += l[i]
        l1.append(s1)

    l2 = [l1[n//2-1]]
    for i in range(n//2, n + n//2 - 1):
        l2 += [l1[i]-l1[i-n//2]]
    l1 = l2

    mn = s
    number = 1

    for i in range(1, n):
        s = s - l1[i] + (value - l1[i])
        if mn > s or mn == s and number > i+1:
            mn, number = s, i+1
    print(number)
