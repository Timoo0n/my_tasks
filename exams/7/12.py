
def f(s):
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s: s = s.replace('>1', '22>', 1)
        if '>2' in s: s = s.replace('>2', '2>1', 1)
        if '>3' in s: s = s.replace('>3', '1>', 1)
    return s

s = '>' + '3'*25 + '1'*15 + '2'*20  
print(sum(list(map(int, f(s).replace('>', '')))))

