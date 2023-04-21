s = 'АБВГД БВЕ ВЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛКМ'
d = {i[0]: i[1:] for i in s.split()}

def f(s, end):
    if s[-1] == end: return len(s)-1
    return max(f(s+i,end) for i in d[s[-1]])
print(f('А', 'М'))
