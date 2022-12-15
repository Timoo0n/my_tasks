def f():
    for x in range(80):
        result = 5 + 7*80 + x*80**2 + 3*80**3 + x*80 + 4*80**2 + 1*80**3
        if result % 17 == 0:
            print(x, result//17)


if __name__ == '__main__': f()
