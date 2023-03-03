for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n, k, m = map(int, file.readline().split())
        l = []
        for _ in range(n):
            km, weight = map(int, file.readline().split())
            number = weight // 9 if weight % 9 == 0 else weight // 9 + 1
            l.append([km, number])

        value = max(l, key=lambda el: el[0])[0]+1
        road = [0]*value
        for km, number in l:
            road[km] = number
        road *= 2

        s = mx = sum(road[:2*m+1])
        for i in range(m+1, value+m):
            s = s + road[m+i]-road[i-m-1]
            if road[i]: mx = max(mx, s)
        print(mx)
