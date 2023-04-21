with open('26_7602.txt', 'r', encoding='utf-8') as file:
    k, n = [int(file.readline()) for _ in range(2)]
    l = sorted([[int(j) for j in file.readline().split()] for _ in range(n)], key=lambda el: el[0])
    l1 = [0]*k
    count = 0
    for i in range(k):
        l1[i] = l[0][1]
        count += 1
        l.pop(0)

    while l:
        first, second = l[0][0], l[0][1]
        for i in range(k):
            if l1[i] < first:
                l1[i] = second
                if len(l) == 1:
                    print(i+1)
                l.pop(0)
                count += 1
                break
        else:
            l.pop(0)
    print(count)
