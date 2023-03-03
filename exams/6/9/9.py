with open('9.csv', 'r') as file:
    l = [list(map(int, i.split(';'))) for i in file]
    c = 0
    for i in l:
        if i[0] == i[2] and i[1] == i[3] and sum(i) == 360: c +=1
    print(c)
