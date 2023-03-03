with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [ [0, 0] ]
    collection = []
    for _ in range(n):
        num = int(file.readline())
        l = [[num+num1, length+1] for num1, length in l] + [ [num, 1] ]
        l = {s[0] % 69: s for s in sorted(l, key=lambda el: el[0])}
        if 0 in l.keys(): collection += [l[0][1]]
        l = list(l.values())
    print(max(collection))
