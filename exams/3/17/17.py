
with open('17.txt', 'r', encoding='utf-8') as file:
    l = [int(i) for i in file.read().strip().split()]
    value = abs(max(l)+min(l))

    l1 = []
    for i in range(1, len(l)):
        if l[i] > value and l[i-1] > value:
            if '31' not in (str(l[i])[-2:], str(l[i-1])[-2:]):
                l1 += [l[i]+l[i-1]]
    print(len(l1))
                
