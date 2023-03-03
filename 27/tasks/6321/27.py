for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n, v, m = map(int, file.readline().split())
        l = []
        for _ in range(n):
            km, number = map(int, file.readline().split())
            number = number // v if number % v == 0 else number // v + 1
            l.append([km, number])

        value = max(l, key=lambda el: el[0])[0]+1
        k = [0]*(value)  # Автомагистраль
        for km, number in l:
            k[km] = number

        s = sum(k[:2*m+1])
        mx = float('-inf')
        for i in range(m+1, value-m):
            s = s-k[i-m-1]+k[i+m]
            if k[i]>0: mx = max(mx, s)
        print(mx)
