with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.read().replace('G', ' ').replace('W', ' ').replace('P', ' ').split()
    print(max(len(i) for i in s))
