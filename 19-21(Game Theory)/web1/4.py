 
def f(a, b, c, m):
    if a+b <= 20: return c % 2 == m % 2
    if c == m: return 0

     
    
    l = [f(a-1,b,c+1,m), f(a, b-1,c+1,m), f(a//2+a%2,b,c+1,m), f(a,b//2+b%2,c+1,m)]

    return any(l) if (c+1)%2 == m%2 else all(l)


for s in range(11, 50):
    for m in range(1, 5):
        if f(10, s, 0, m)==1:
            print(s, m)
            break
