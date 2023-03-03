with open('9.csv', 'r') as file:
    l = [[int(j) for j in i.strip().split(';')] for i in file]
    c = 0
    for my_list in l:
        if len(my_list) == len(set(my_list)):
            l1 = [i for i in my_list if i % 2 == 1]
            l2 = [i for i in my_list if i % 2 == 0]
            if len(l2) > len(l1): c += 1
    print(c)
