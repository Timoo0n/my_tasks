with open('17.txt', 'r', encoding='utf-8') as file:
    l = [int(i) for i in file]
    max_value = max(i for i in l if abs(i) % 11 == 0)

    l1 = []
    for i in range(len(l)-1):
        if ((abs(l[i]) % 11 == 0) or (abs(l[i+1]) % 11 == 0)) and ((l[i]+l[i+1]) <= max_value):
            l1 += [l[i+1]+l[i]]
    print(len(l1), max(l1))
