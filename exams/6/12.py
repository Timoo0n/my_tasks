def f(s):
    while '111' in s or '333' in s:
        if '111' in s: s = s.replace('111', '3', 1)
        else: s = s.replace('333', '1', 1)
    return sum(list(map(int, s)))

l = []
for i in range(100, 1000):
    l += [[i, f('3'*i)]]
print(min(l, key=lambda el: el[1]))
