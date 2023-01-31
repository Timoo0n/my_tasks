with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l0 = [0]*80  # меньше 50_000
    l1 = [0]*80  # больше 50_000
    count = 0
    
    for i in range(n):
        num = int(file.readline())

        remainder = 0 if num % 80 == 0 else 80 - (num % 80)

        if num > 50_000:  count += l0[remainder] + l1[remainder]
        else: count += l1[remainder]

        if num > 50_000: l1[num % 80] += 1
        else: l0[num % 80] += 1
    print(count)
