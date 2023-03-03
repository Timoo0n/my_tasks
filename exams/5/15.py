def f(x, y, a):
    return (2*y + 3*x != 135) or (y > a) or (x > a)

for a in range(100):
    if all(f(x, y, a) for x in range(1000) for y in range(1000)):
        print(a)
