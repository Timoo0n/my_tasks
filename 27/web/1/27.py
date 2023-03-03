for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n, m = list(map(int, file.readline().split()))
        l = []
        for _ in range(n):
            num = int(file.readline())
            num = num//6 if num % 6 == 0 else num//6+1
            l += [num]
        ms = float('-inf')
        s = sum(l[:2*m+1])
        for i in range(m+1, n-m):
            s = s+l[m+i]-l[i-m-1]
            ms = max(s, ms)
        print(ms)
