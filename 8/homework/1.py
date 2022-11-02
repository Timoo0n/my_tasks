from itertools import product


def f1():
    my_list = [1 for i in product('КРЕСЛО', repeat=4) if ''.join(i)[-1] in 'ЕО' and ''.join(i)[0] in 'КРСЛ']
    return sum(my_list)


def f2():
    my_list = [1 for i in product('ABCWXYZ', repeat=6) if all(''.join(i)[j] in 'WXYZ' for j in (0, -1)) and all(''.join(i)[j] in 'ABC' for j in range(1, 5))]
    return sum(my_list)


def f3():
    return sum([1 for i in product('ПУЛЯ', repeat=6) if ''.join(i).count('У') == 2])


if __name__ == '__main__':
    print(f3())
