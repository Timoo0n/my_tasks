
def f(n):
    if n <= 1: return 0
    return int(f(n-1) + 3 * n**2) if n > 1 and n % 2 != 0 else int(n / 2 + f(n-1) + 2)

print(f(49))
