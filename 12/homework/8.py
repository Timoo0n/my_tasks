
s = '112'*4+'11'*2

while '11' in s:
    if '112' in s: s = s.replace('112', '7', 1)
    else: s = s.replace('11', '3', 1)


print(sum(list(map(int, list(s)))))
