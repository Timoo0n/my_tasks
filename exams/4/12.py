n = 2
 

def f(s):
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s: s = s.replace('>1', '22>3', 1)
        if '>2' in s: s = s.replace('>2', '2>', 1)
        if '>3' in s: s = s.replace('>3', '11>2', 1)
    return s

c = 0
for n in range(3, 51):
    s = '>' + '1'*n+'2'*n+'3'*n
    r = sum([int(i) for i in f(s)[:-1]])
    if r % 7 == 0: c += 1
print(c)
