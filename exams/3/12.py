def alg(s):
    while '>1' in s or '>3' in s or '>2' in s:
        if '>1' in s: s = s.replace('>1', '1>', 1)
        if '>3' in s: s = s.replace('>3', '>2', 1)
        if '>2' in s: s = s.replace('>2', '>1')
    return s

def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


for n in range(1000):
    s = '>' + '1' * 16 + '2' * n + '3' * 16
    result = alg(s).replace('>', '')
    summ = sum(int(i) for i in result)
    if p(summ): print(n); break
    
