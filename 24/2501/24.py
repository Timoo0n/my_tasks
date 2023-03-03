with open('2501_24.txt', 'r', encoding='utf-8') as file:
    l = file.read()
    count = 0
    for i in range(len(l)-4):
        if l[i] == 'A' and l[i+2] == 'A'\
           and l[i+4] == 'A': count += 1
    print(count)
