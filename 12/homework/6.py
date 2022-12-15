
s = '>' + '1'*11 + '2'*12 + '3'*30

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s: s = s.replace('>1', '22>', 1)
    elif '>2' in s: s = s.replace('>2', '2>', 1)
    elif '>3' in s: s = s.replace('>3', '1>', 1)

print(sum(list(map(int, list(s[:-1])))))
