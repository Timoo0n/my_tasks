from itertools import product, permutations


def f():
    return len(list(filter(lambda el: 'X' in el[:2], [''.join(i) for i in product('ABCX', repeat=5) if i[-1] == 'X'])))


def f1():
    return sum([1 for _ in set(permutations('АСCACИН'))])


def f2():  # -
    return sum([1 for i in set(permutations('ПЕСКАРЬ')) if ''.join(i)[0] != 'Ь' and all(j not in ''.join(i) for j in ('ЬА', 'ЬЕ', 'ЬР'))])


def f3():  # -
    return sum([1 for i in set(permutations('КОЛУН')) if all(''.join(j) not in ''.join(i) for j in product('КЛН', repeat=2)) and all(''.join(j) not in ''.join(i) for j in product('ОУ', repeat=2))])


def f4():  # -
    return len([''.join(i) for i in product('01234567', repeat=4) if all(int(''.join(i)[j-1]) >= int(''.join(i)[j-1]) for j in range(1, len(i)))])


def f6():
    return sum([1 for i in set(permutations('ИГРОК')) if i[0] != 'К' and 'РОК' not in ''.join(i)])


def f7():
    return sum([1 for i in permutations('АБИКОЛУН') if all(''.join(j) not in ''.join(i) for j in product('АИОУ', repeat=2)) and all(''.join(j) not in ''.join(i) for j in product('БКЛН', repeat=2))])


def f8():
    return sum([1 for i in product('AB123', repeat=8) if i.count('A') + i.count('B') == 2 and sum([i.count(j) for j in ('1', '2', '3')]) == 6])


def f9():
    return sum([1 for i in product('01234', repeat=6) if i[0] != '1' and i[0] != '0' and all(i[-1] != j for j in ('3', '4'))])


def f10():
    return sum([1 for i in product('ВИШНЯ', repeat=6) if i[0] != 'Ш' and i.count('В') <= 1 and i[-1] not in 'ИЯ'])


def f11():
    return sum([1 for i in product('ABCD', repeat=4) if ''.join(i) == ''.join(sorted(i))])


def f12():
    return sum([1 for i in product('ГЕПАРД', repeat=5) if i.count('Г') == 1 and i[0] != 'А' and i[-1] != 'Е'])


def main():
    print(f12())


if __name__ == '__main__':
    main()
