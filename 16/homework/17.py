
def f(n):
    s = 1
    if n >= 1:
        s += 1 + f(n-1) + f(n - 3) + 1
    return s

print(f(40))
        
