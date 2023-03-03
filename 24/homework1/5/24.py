with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.readline()
    while 'XIXIX' in s: s = s.replace('XIXIX', 'XIX XIX')
    print(s.count('XIX'))
