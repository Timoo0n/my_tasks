with open('27B.txt', 'r', encoding='utf-8') as file:
    l = [0]*131
    n = int(file.readline())
    count = 0

    for i in range(n):
        num = int(file.readline())

        ind = 131 - (num % 131) if num % 131 != 0 else 0
        count += l[ind]

        l[num % 131] += 1
    print(count)
