from string import ascii_lowercase, digits


class Homework:
    def __init__(self, *args, **kwargs):
        print('Homework: ')

    def __repr__(self):
        return 'Homework)'

    @staticmethod
    def f1():
        return str(oct(64**30+2**300-4))[2:].count('7')

    @staticmethod
    def f2():
        num = 3*16**8-4**5+3
        my_list = []

        while num > 0:
            my_list = [num % 4] + my_list

            num //= 4

        return my_list.count(3)

    @staticmethod
    def f3():
        num = 2*27**7+3**10-9
        my_list = []

        while num > 0:
            my_list = [num % 3] + my_list

            num //= 3

        return my_list.count(0)

    @staticmethod
    def f4():
        num = 51*7**12-7**3-22
        my_list = []
        while num > 0:
            my_list = [num % 7] + my_list

            num //= 7

        return sum(my_list)

    @staticmethod
    def f5():
        for x in range(1, 1000):
            num = 125**200-5**x+74
            my_list = []

            while num > 0:
                my_list = [num % 5] + my_list

                num //= 5

            if my_list.count(4) == 100:
                return x

    @staticmethod
    def f6():
        for x in range(1, 10000):
            if str(bin(4**2015+2**x-2**2015+15)).count('1') == 500:
                return x

    @staticmethod
    def f7():
        for x in range(1, 10000):
            if str(bin(4**1014-2**x+12)).count('0') == 2000:
                return x

    @staticmethod
    def f8():
        for x in range(1, 10001):
            num = 36**17-6**x+71
            my_list = []

            while num > 0:
                my_list = [num % 6] + my_list

                num //= 6

            if sum(my_list) == 61:
                return x

    @staticmethod
    def f9():
        count = 0
        num = 6*144**26 + 11*12**75 - 48

        while num > 0:
            if num % 12 == 11:
                count += 1

            num //= 12

        return count

    @staticmethod
    def f10():
        num = 5*216**1156 - 4*36**1147 + 6**1153 - 875
        my_list = []

        while num > 0:
            my_list = [num % 6] + my_list

            num //= 6

        return abs(my_list.count(5) - my_list.count(0))

    @staticmethod
    def f11():
        for x in range(2, 1000):
            if 3*(x+4) + 3 - 3*4 - 3 == 33:
                return x

    @staticmethod
    def f12():
        for n in range(1, 100):
            if 1*n**2+3 == 9*(n+2) + 7:
                return n

    @staticmethod
    def f12_1():
        for n in range(1, 36):
            try:
                if int('103', n) == int('97', n+2):
                    return n
            except ValueError:
                continue

    @staticmethod
    def f13():
        for n in range(1, 100):
            if n**2+3*n+2 + 1*8+3 == 1*(n+1)**2 + 2*(n+1) + 4:
                return n

    @staticmethod
    def f13_1():
        for n in range(1, 36):
            try:
                if int('132', n) + int('13', 8) == int('124', n+1):
                    return n
            except ValueError:
                continue

    @staticmethod
    def f14():
        for x in range(1, 1000):
            if (2*x+1)*(x+3) == (3*x**2+x+3):
                return x

    @staticmethod
    def f15():
        for x in range(20, 31):
            if x % 3 == 1 and x // 3 % 3 == 1:
                return x

    @staticmethod
    def f16():
        my_list = []
        for x in range(10, 41):
            if str(bin(x))[-4:] == '1011':
                my_list.append(x)

        return max(my_list)

    @staticmethod
    def f17():
        num = 68
        for n in range(1, 10000):
            if (num % n == 2) and (n**3 <= num < n**4):
                return n

    @staticmethod
    def f18():
        for n in range(1, 1000):
            if 6 <= n < 36 and 5**2 <= n < 5**3 and n % 11 == 1:
                return n

    @staticmethod
    def f19():
        for n in range(1, 1000):
            if 7 <= n < 7**2 and 6**2 <= n < 6**3 and n % 13 == 3:
                return n

    @staticmethod
    def f20():
        my_list = []
        for n in range(1, 10000):
            if 4**2 < n < 5**4 and n % 16 == 12:
                my_list.append(n)

        return len(my_list)

    @staticmethod
    def f21():
        for x in range(1, 10000):
            num = (5 + x*15 + 3*15**2 + 2*15**3 + 15**4) + (3 + 3*15 + 2*15**2 + x*15**3 + 15**4)
            if num % 14 == 0:
                return num // 14

    @staticmethod
    def f22():
        for x in range(1, 10000):
            num = (x + 9*17 + 5*17**2 + 7*17**3 + 9*17**4) + (8 + 17**2 + x*17**3 + 3*17**4)
            if num % 11 == 0:
                return num // 11

    @staticmethod
    def f23():
        for x in range(1, 10000):
            if (x + 4*11 + 6*11**2 + 3*11**3 + 3*11**4) + (6 + 4*12 + 9*12**2 + 7*12**3 + x*12**4) == (7 + 8*14 + x*14**2 + 5*14**3 + 5*14**4):
                return 7 + 8*14 + x*14**2 + 5*14**3 + 5*14**4

    @staticmethod
    def f24():
        for x in range(0, 15):
            for y in range(0, 17):
                num = (5 + x*15 + 3*15**2 + 2*15**3 + 15**4) + (9 + y*17 + 7*17**2 + 6*17**3)
                if num % 131 == 0:
                    print(y, num // 131)

    @staticmethod
    def f24_1():
        my_list = []
        for x in '0123456789abcde':
            for y in '0123456789abcdefg':
                num = int(f'123{x}5', 15) + int(f'67{y}9', 17)
                if num % 131 == 0:
                    my_list.append((int(y, 17), num // 131))

        return min(my_list, key=lambda el: el[0])[1]

    @staticmethod
    def f25():
        x_list = []
        for x in range(1, 21):
            my_list = []
            for y in range(1, 21):
                num = (9 + x*21 + y*21**2 + 2*21**3 + 21**4) + (9 + 9*21 + y*21**2 + 6*21**3 + 3*21**4)
                my_list.append(num)

            if all(i % 18 == 0 for i in my_list):
                x_list.append((x, my_list[4] // 18))

        return min(x_list, key=lambda el: el[0])[1]

    @staticmethod
    def f25_1():
        x_list = []
        for x in digits + ascii_lowercase[:11]:
            my_list = []
            for y in digits + ascii_lowercase[:11]:
                num = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
                my_list.append(num)

            if all(i % 18 == 0 for i in my_list):
                x_list.append((int(x, 21), my_list[5] // 18))

        return min(x_list, key=lambda el: el[0])[1]


if __name__ == '__main__':
    homework = Homework()
    print(homework.f25())
