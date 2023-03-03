with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [0]*7
    min_s = 0

    for _ in range(n):
        num, num1 = sorted(list(map(int, file.readline().split())))
        min_s += num

        for i in [num + value for value in l] + [num1 + value for value in l]:
            l[i % 7] = max(l[i % 7], i)
    print(max(i for i in l if i % 7 == min_s % 7))
