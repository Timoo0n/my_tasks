def f():
    for x in '0123456789abcdefgh':
        result = (int(f'9009{x}', 18) + int(f'2257{x}', 18))
        if result % 15 == 0:
            return x, result // 15


def f1():
    for x in range(18):
        num = 2*x + 11*18**4 + 16*18 + 2*18**3 + 5*18**2  # Поделили на разряды 2 числа
        if num % 15 == 0:
            return x, num // 15

 
if __name__ == '__main__':
    print(*f1())