
my_set = set()

def f(c, s):
    if s == 15: my_set.add(c)
    else:
        f(c*2, s+1)
        f(c*2+1, s+1)

f(1, 0)

print(len(my_set))
    
