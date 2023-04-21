for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n, m = map(int, file.readline().split())
        l = []
        s = 0
        for _ in range(n):
            km, num = map(int, file.readline().split())
            num = num // m if num % m == 0 else num // m + 1
            s += num
            l.append([km, num, s])

        s0 = 0
        for i in range(n):
            s0 += l[i][1]*(l[i][0]-l[0][0])

        mn = s0
        for i in range(1, n):
            delta = l[i][0]-l[i-1][0]
            s0 = s0 + delta*l[i-1][2]-delta*(s-l[i-1][2])
            mn = min(mn, s0)
        print(mn)
        
    
