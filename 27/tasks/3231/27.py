for word in 'AB':
    with open(f'27-{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [int(i) for i in file]

        value = sum(min(i, n-i)*l[i] for i in range(n))
        l *= 2
        l1 = []
        s = 0
        for i in range(2*n):
            s += l[i]
            l1.append(s)

        mn = value
        position = 0
        for i in range(1, n):
            value = value - (l1[n//2+i-1] - l1[i-1]) + (l1[n+i-1]-l1[n//2+i-1])
            if value < mn:
                mn, position = value, i+1
        print(position)
            
    
# 8
# 41495
