with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    l = [int(i) for i in file]

    my_l = [l.count(i) for i in set(l)]

    print(len(my_l), max(my_l))
        
