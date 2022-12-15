def f1(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0: my_set |= {num//i, i}

    return sorted(my_set)


def f():
    for i in range(1_000):
        for j in range(10):
            num = int(f'3{i}52{j}')
            result = f1(num)
            if len(result) % 2 == 1:
                print(num, max(result))
            


if __name__ == '__main__':f()
