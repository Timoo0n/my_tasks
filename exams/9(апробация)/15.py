def f(x,y,a):
    return (x+y <= 32) or (y <= x+4) or (y >= a)

for a in range(100):
    if all(f(x,y,a) for x in range(1000) for y in range(1000)):
        print(a)
