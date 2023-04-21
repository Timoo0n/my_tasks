s = 'АВЗ БГА ВЗКЕБ ГА ДГА ЕБ ИД ЗИЖК ЖИ КЕЖ'
d = {i[0]: i[1:] for i in s.split()}

def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+i, end) for i in d[s[-1]])
print(f('В', 'А')+f('З', 'А'))
