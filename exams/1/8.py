from itertools import product

def f():
    count = 0
    for i in product('АРБУЗ', repeat=6):
        if (i.count('А') == 3) and ('АА' in ''.join(i)) and ('ААА' not in ''.join(i)):
            count += 1
    print(count)


if __name__ == '__main__': f()
