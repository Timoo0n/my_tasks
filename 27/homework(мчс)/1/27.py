
for word in ['A', 'B']:
    with open(f'27-{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [0]

        for _ in range(n):
            pair = list(map(int, file.readline().split()))
            l = [num +num1 for num in pair for num1 in l]
            l = {i%3:i for i in sorted(l)}.values()
        print(max(i for i in l if i % 3 != 0))
