
my_set = set()
def f(cur, step):
    if step == 13: my_set.add(cur)
    else: f(cur+3, step+1); f(cur*2+1, step+1)
f(2, 0)

print(len(my_set))
