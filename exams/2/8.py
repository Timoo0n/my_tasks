from itertools import product

def f():
    count = 0
    for i in product('012345678', repeat=5):
        num = ''.join(i)
        if int(num[0]) % 2 == 0 and num[-1] not in ('1', '8') and num.count('3') <= 1 and len(str(int(num))) == 5:
            count += 1
    print(count)


def main(): f()


if __name__ == '__main__': main()
