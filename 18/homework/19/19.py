with open('t.txt', 'r', encoding='utf-8') as file:
    s = list(map(lambda el: [float(i.replace(',', '.')) for i in el.split('\t')], file.read().strip().split('\n')))
    l = list()
    for i in range(len(s)):
        value = int(s[i][1])
        if value == 0:
            s[i] = '--'
        else:
            s[i] = f' {s[i][0]} '
    s = list(map(lambda el: sum([float(i) for i in el.split()]), list(filter(lambda el: el != '', ''.join(s).split('--')))))
    print(max(s))
