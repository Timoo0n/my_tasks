
def new_num(num):
    new_num = list(map(lambda el: str(el+1) if el != 9 else str(el), list(map(int, str(num)))))
    return int(''.join(new_num))


def f(c, e):
    if c > e: return 0
    elif c == e: return 1
    return f(c+1, e) + f(new_num(c), e)


print(f(25, 51))

 
