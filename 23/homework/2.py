
def f(c, e):
    if c > e: return 0
    elif c == e: return 1
    return f(c+1, e)+f(c*2, e)+f(c**2, e)
print(f(5, 154))


my_list = []
def f1(c, e):
    if c <= e: my_list.append(c)
    if c <= e: f1(c+1, e); f1(c*2, e); f1(c**2, e)

f1(5, 154)
print(my_list.count(154))



def f2():
    l = [0]*200
    l[5] = 1

    for i in range(len(l)):
        if i + 1 <= 154: l[i + 1] += l[i]
        if i**2 <= 154: l[i**2] += l[i]
        if i*2 <= 154: l[i*2] += l[i]
    return l[154]

print(f2())
