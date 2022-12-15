def f():
    count = 0
    for x in range(-100, 1000):
        for y in range(-100, 1000):
            if y < 3 * x and y > 0 and y < 15 and y > (x / 4 - 14):
                count += 1
    print(count)
                

if __name__ == '__main__': f()
