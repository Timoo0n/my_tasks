
def f(c, e):
    if c > e: return 0
    elif c == e: return 1
    return f(c+1, e)+f(c+3, e)+f(c*2, e)


my_list = []
def f1(c, e):
    if c <= e: my_list.append(c)
    if c <= e: f1(c+1, e); f1(c+3, e); f1(c*2, e)
f1(1, 15)

def f2():
    l = [0]*100
    l[1] = 1
    
    for i in range(1, len(l)):
       if i + 1 <= 15: l[i+1] += l[i]
       if i + 3 <= 15: l[i+3] += l[i]
       if i * 2 <= 15: l[i*2] += l[i]
    return l
       
        

print(f(1, 15), my_list.count(15), f2())
