def f(n):
    if n < 0: return -n
    if n % 2 == 0: return 2*n+1+f(n-3)
    if n % 2 == 1: return 5*n+2*f(n-4)
print(f(33))
