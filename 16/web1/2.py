

def f(n):
    if int(n**0.5)**2 == n: return n**0.5
    else: return f(n+1)+1

print(f(4850)+f(5000))
