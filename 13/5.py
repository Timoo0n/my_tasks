s = 'АБГД БГВ ВГЕИ ГДЖЕ ДЖ ЕИКМ ЖЕК ИМ КМ'
d = {i[0]: i[1:] for i in s.split()}

def f(s, end):
    if s[-1] == end: return len(s) == 7
    return sum(f(s+i, end) for i in d[s[-1]])
print(f('А', 'М'))
