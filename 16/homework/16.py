def f(n):
    if n == 1: return 1
    return f(n // 2) + 1 if n % 2 == 0 else f(n - 1) + n


def main():
    r = 0
    c = 0
    
    while r != 19:
        c += 1
        r = f(c)  
    print(c)


main()
        
