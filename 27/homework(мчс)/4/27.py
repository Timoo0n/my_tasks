
for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [0]

        for _ in range(n):
            tr = list(map(int, file.readline().split()))
            tr = [tr[0]+tr[1], tr[1]+tr[2], tr[0]+tr[2]]
            l = [num+num1 for num in tr for num1 in l]
            l = {num%4: num for num in sorted(l)}.values()
        print(max(i for i in l if i % 4 == 0))

