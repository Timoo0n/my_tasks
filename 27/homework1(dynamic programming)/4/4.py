with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    l = [0]*131
    count = 0

    for i in range(info):
        n = int(file.readline())

        remainder = 0 if n % 131 == 0 else 131 - (n % 131)

        count += l[remainder]
        l[n % 131] += 1

    print(count)

        
