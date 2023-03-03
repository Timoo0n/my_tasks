for word in 'ab':
    with open(f'27_4605{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = []
        s1 = 0
        for _ in range(n):
            km, num = map(int, file.readline().split())
            num = num // 36 if num % 36 == 0 else num // 36 + 1
            s1 += num
            l.append([km, num, s1])
        s = 0
        for i in range(n):
            s += l[i][1]*(l[i][0]-l[0][0])
        mn = s
        for i in range(1, n):
            r = l[i][0]-l[i-1][0]
            s = s + r*l[i-1][2] - r*(s1-l[i-1][2])
            mn = min(mn, s)
        print(mn)
        
    
        
