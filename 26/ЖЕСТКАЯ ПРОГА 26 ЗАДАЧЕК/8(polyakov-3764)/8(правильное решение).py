with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = sorted([int(i) for i in file])

    values_l = []
    for i in range(info):
        for j in range(i+1, info):
            sum_value = l[i] + l[j]

            if sum_value % 2 == 0:
                avg = sum_value // 2

                K = min(abs(l[x]-avg) for x in range(i, j+1))
                if K == 5: values_l += [avg]
    print(values_l)
