s = 'АБГ БД ВБАГДЖ ГЖ ДИЕ ЕВЛК ЖЕ ИЕЛ КЖ ЛК'
d = {i[0]:i[1:] for i in s.split()}

def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+i, end) for i in d[s[-1]])
print(f('Л', 'Е')+f('К', 'Е')+f('В', 'Е'))
