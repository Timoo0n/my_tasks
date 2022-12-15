def f():
    count = 0
    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            if 3*x > y and x < y and y < 90:
                count += 1
    print(count)


if __name__ == '__main__': f()
