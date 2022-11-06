from itertools import product


def f():
    count = 0
    for num in range(100_000, 1_000_000):
        n = str(num)
        if len(n) == len(set(n)) and num % 5 == 0:
            if all(''.join(i) not in n for i in product('02468', repeat=2)) and all(''.join(i) not in n for i in product('13579', repeat=2)):
                count += 1
    return count


if __name__ == '__main__':
    print(f())