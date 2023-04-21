s = 'АБГД БВГ ВЕКЗ ГВЕЖ ДГ ЕЖИКМ ЖИ ЗКЛ КЛНМ ИМ МН ЛН'
d = {i[0]:i[1:] for i in s.split()}
l = []
def f(s, end):
    if s[-1] == end:
        if len(s) == 8: l.append(s)
        return len(s) == 8
    return sum(f(s+i,end) for i in d[s[-1]])

f('А', 'Н')
for i in l:
    if i == ''.join(sorted(i)): print(i)
