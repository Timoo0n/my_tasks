
for word in 'AB':
    with open(f'27-{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [0] # список всех возможных сумм
        for _ in range(n):
            pair = list(map(int, file.readline().split()))
            l = [num+num1 for num in pair for num1 in l]
            l = {i%5: i for i in sorted(l)[::-1]}.values()
        print(min(i for i in l if i % 5 != 0))
    
