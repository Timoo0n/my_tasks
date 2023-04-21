with open('17_6752.txt', 'r', encoding='utf-8') as file:
    l = [int(i) for i in file]
    value = len([i for i in l if abs(i) % 3 == 0])
    collection = list()
    for i in range(1, len(l)):
        num, num1 = l[i-1],l[i]
        if (num < 0 or num1 < 0) and num+num1<value:
            collection.append(num+num1)
    print(len(collection), max(collection))
            
