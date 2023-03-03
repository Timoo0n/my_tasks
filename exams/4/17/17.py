with open('17.txt', 'r', encoding='utf-8') as file:
    l = [int(i) for i in file]
    value = sum(l)/len(l)
    l1 = []
    for i in range(len(l)-2):
        l2 = [l[i], l[i+1], l[i+2]]
        if any(i < value for i in l2) and all('9' in str(i) for i in l2):
            l1.append(sum(l2))
    print(len(l1), max(l1))
