def f(x, a):
    return (x % a == 0) or ((x % 23 == 0) <= (not (x in list(range(50, 71)))))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
