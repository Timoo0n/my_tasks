

def f1(n):
    if n < 3: return n + 1
    elif n >= 3 and n % 2 == 0: return f1(n-2) + n - 2
    elif n >= 3 and n % 2 != 0: return f1(n+2) + n + 2
    

def f(n):
    l = [0]*n
    for i in range(len(l)):
        n = i + 1
        if n < 3: l[i] = n + 1
        elif n >= 3 and n % 2 == 0: l[i] = l[i-2] + n - 2
    return l


print(len(list(filter(lambda el: len(str(el)) == 5, f(10**5)))))

