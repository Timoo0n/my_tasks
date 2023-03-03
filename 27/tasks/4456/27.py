for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        q = []
        s = 0
        for i in range(100):
            num = int(file.readline())
            s += num
            q += [s]
        l = [0]*999
        count = 0

        for _ in range(n-100):
            num = int(file.readline())
            s += num
            if s % 999 == 0: count += 1
            count += l[s%999]

            s1 = q.pop(0)
            l[s1%999] += 1
            q += [s]
        print(count)
 
