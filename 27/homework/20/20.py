with open('27B.txt') as file:
    k = k1 = k2 = k3 = 0
    info = int(file.readline())

    for _ in range(info):
        x, y = map(int, file.readline().split())
        if x == 0 and y == 0: k += 1
        elif x == 0: k1 += 1
        elif y == 0: k2 += 1
        else: k3 += 1
    print(k*k1*k3 + k*k2*k3 + k1*k2*k3)
