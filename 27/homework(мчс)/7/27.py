with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = []
    collection = []
    for _ in range(n):
        num = int(file.readline())
        l = [num+num1 for num1 in l] + [num]
        l = {num%1000:num for num in sorted(l)}
        if 0 in l.keys(): collection += [l[0]]
        l = l.values()
    print(max(i for i in collection if i % 1000 == 0))
