
for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [ [0, 0] ]
        collection = []
        for _ in range(n):
            num = int(file.readline())
            l = [[num+num1, number+int(num % 5 == 0)] for num1, number in l] + [[num, int(num % 5 == 0)]]
            l = {s[1]%3:s for s in sorted(l)}
            if 0 in l.keys():
                collection += [l[0][0]]
            l = list(l.values())
        print(max(collection))
