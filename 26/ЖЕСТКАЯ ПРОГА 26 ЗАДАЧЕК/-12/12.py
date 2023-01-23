with open('26-66.txt', 'r', encoding='utf-8') as file:
    n, k = map(int, file.readline().split())
    l = [0]*(24*3600*1000+1)

    s = k; e = k + 24*3600*1000

    for i in range(n):
        st, end = map(int, file.readline().split())
        if (st < e or st == 0) and (end > s or end == 0):
            if st < s or st == 0:
                st = s
            if end > e or end == 0:
                end = e
            l[st-s] += 1
            l[end-s] -= 1
    mx = 0
    count = 0
    k = 0
    for i in range(len(l)):
        k += l[i]
        if k > mx: mx, count = k, 0
        elif k == mx: count += 1
    print(mx, count)

