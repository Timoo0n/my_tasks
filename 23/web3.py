
my_set = set()
def f(cur, end):
    if cur < end and cur % 2 == 0: my_set.add(cur)
    if cur < end: f(cur+3, end); f(cur*3, end)


f(3, 100)
print(len(my_set))
