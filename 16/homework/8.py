
def f(n):
    if n in (1, 2): return n
    elif n > 2 and n % 2 == 0: return int((n+f(n-2))/5)
    return int( (2*n+f(n-1)+f(n-2))/4)

print(f(50))
