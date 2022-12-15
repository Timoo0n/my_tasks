
def f(n):
    f = {i: 0 for i in range(n+1)}

    for n in f.keys():
        if n == 1: f[n] = 1
        elif n == 2: f[n] = 2
        elif n > 2: f[n] = n*(n-1)+f[n-1]+f[n-2]
    return f[n]

print(f(2023)-f(2022)-f(2020)-f(2019))
