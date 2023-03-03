for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n, m = map(int, file.readline().split())
        l = [int(i) for i in file]
        s = mx = sum(l[:2*m+1])
        l = l*2

        for i in range(m+1, n+m):
            s = s-l[i-m-1]+l[i+m]
            mx = max(mx, s)
        print(mx)
