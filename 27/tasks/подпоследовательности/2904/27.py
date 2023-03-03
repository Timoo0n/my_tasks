with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    ms = float('inf')

    k = [float('-inf')]*2077
    k1 = [0]*2077

    s0 = 0
    len0 = float('-inf')

    for i in range(n):
        num = int(file.readline())
        s0 += num

        if s0 % 2077 == 0 and s0 < ms:
            ms = s0
            len0 = max(i+1, len0)

        s1 = s0 - k[s0 % 2077]
        len1 = i+1 - k1[s0 % 2077]

        if (ms == s1 and len1 > len0) or (ms > s1):
            ms, len0 = s1, len1

        if s0 > k[s0 % 2077]:
            k[s0 % 2077] = s0
            k1[s0 % 2077] = i+1
    print(len0)
            
