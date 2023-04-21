
count = 0
for s in open('24_2503.txt', 'r', encoding='utf-8'):
    while 'OAOAO' in s or 'AOAOA' in s:
        s = s.replace('OAOAO', 'OAO OAO').replace('AOAOA', 'AOA AOA')
    if s.count('AOA') > s.count('OAO'): count += 1
print(count)
