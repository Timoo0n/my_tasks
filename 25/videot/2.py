
def f():
    for i in range(135_790, 163_229):
        my_set = set()
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                my_set |= {j, i//j}

        if sum(my_set) > 460_000:
            print(len(my_set), sum(my_set))


if __name__ == '__main__':
    f()
