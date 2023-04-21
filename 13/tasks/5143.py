s = 'АБВГ БД ВДЕ ГВЕИ ДКЛ ЕДЛЖИ ИЖМН ЖЛМ ЛКМ КМП МПНРС НР РС ПС'
d = {i[0]: i[1:] for i in s.split()}
my_set = set()
def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+i, end) for i in d[s[-1]])
l = [i for i in d.keys()]
count = 0
for i in l:
    count += f(i, 'С')
print(count)
