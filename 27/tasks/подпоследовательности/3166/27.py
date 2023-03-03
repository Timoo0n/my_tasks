with open('27A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    k = 0
    l = [0]*11
    count = 0

    for _ in range(n):
        num = int(file.readline())
        if num % 5 == 0: k += 1
        if k % 11 == 0 and k > 0: count += 1
        count += l[k % 11]

        l[k % 11] += 1
    print(count)
