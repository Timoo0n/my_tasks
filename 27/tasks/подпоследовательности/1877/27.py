with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l = [float('inf')]*69
    l1 = [0]*69

    ms = float('-inf')
    len0 = float('inf')
    s = 0

    for i in range(n):
        num = int(file.readline())
        s += num
        if s % 69 == 0 and s > ms:
            ms = s
            len0 = min(len0, i+1)

        s1 = s - l[s % 69]
        len1 = i+1 - l1[s % 69]

        if (s1 == ms and len1 < len0) or (s1 > ms):
            ms, len0 = s1, len1

        if s < l[s % 69]:
            l[s % 69] = s
            l1[s % 69] = i + 1
    print(len0)
        
        
