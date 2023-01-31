def f(x, a):
    return ((x % 3 == 0) <= (not (x % 17 == 0))) or (not (a < 190 - x))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 10_000)):
        print(a)
        break
