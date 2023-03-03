with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.readline().replace('STOCK', '@')
    print(s.count('OCK'))
