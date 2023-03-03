with open('27-B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l = [int(i) for i in file]
    length = float('-inf')
    for i in range(n):
        if l[i] % 21 == 0 and l[i]**2 in l:
            r1 = l.index(l[i]**2)
            length = max(length, abs(r1-i)+1)
    print(length)
    
