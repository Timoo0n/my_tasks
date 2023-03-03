with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [ [0, 0] ]

    collection = []
    for _ in range(n):
        num = int(file.readline())
        l = [[num+num1, number+1] for num1, number in l] + [ [num, 1] ]
        l = {abs(s[0])%2077: s for s in sorted(l, reverse=True)}
        if 0 in l:
            collection += [l[0]]
        l = list(l.values())
    print(sorted(collection, key=lambda el: el[0]))
