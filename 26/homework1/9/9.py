with open('26.txt', 'r', encoding='utf-8') as file:

    info = int(file.readline())
    my_dict = {i: set() for i in range(1961, 1992)}

    for i in range(info):
        year, c_type = map(int, file.readline().split())
        my_dict[year].add(c_type)

    my_dict = {i: 8 - len(my_dict[i]) for i in my_dict.keys()}  # недостающие 

    print(sum(my_dict.values()))

    for i in reversed(my_dict.keys()):
        if my_dict[i] == max(my_dict.values()):
            print(i)
            break
