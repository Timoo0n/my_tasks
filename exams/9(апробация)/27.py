for word in 'AB':
    with open(f'27_{word}_6760.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [0]*12_000_000
        s = 0
        for _ in range(n):
            km, num = map(int, file.readline().split())
            num = num // 48 if num % 48 == 0 else num// 48 + 1
            l[km]= num
        m = float('inf')
        sm = sum(l)
        c = sum(i*l[i] for i in range(12_000_000))

        before = l[0]
        for i in range(1, 12_000_000):
            c = c + before - (sm-before)
            if l[i]: m = min(m, c)
            before += l[i]
        print(m)
       
