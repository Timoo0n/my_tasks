from itertools import product


def f():
    count = 0
    for my_tuple in product('АБРТЫ', repeat=5):
        my_str = ''.join(my_tuple)
        count += 1

        if 'Ы' not in my_str and 'АА' not in my_str:
            print(my_str, count)
            break


if __name__ == '__main__':
    f()