with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = sorted([int(i) for i in file])
    weight = [0]*(sum(l)+1)

    for i in range(info):
        weight2 = weight.copy()
        for j in range(len(weight)):
            if weight[j] > 0:
                weight2[j+l[i]] += weight[j]
        weight2[l[i]] += 1
        weight = weight2
    print(weight[100])
