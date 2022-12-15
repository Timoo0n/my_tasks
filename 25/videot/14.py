
def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


for i in range(50_000_000, 50_500_001):
    if int(i**0.5)**2 == i and p(i):
        print(2*int(i**0.5)**2,  int(i**0.5))
