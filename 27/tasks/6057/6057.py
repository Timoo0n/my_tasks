with open('27_B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [0,0,0]
    collection = []
    for _ in range(n):
        tr = list(map(int, file.readline().split()))
        l = [num+num1 for num1 in l for num in tr]
        l = {int(s%91!=0):s for s in sorted(l)}
        if 1 in l.keys(): collection += [l[1]]
        l = list(l.values())
    print(max(collection))
