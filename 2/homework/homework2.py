from itertools import product


class Homework2:
    def __init__(self):
        self.__my_list = product(range(2), repeat=4)

    def f2_17(self):
        print('A B C D')
        for a, b, c, d in self.__my_list:
            if not((not a and not b) or (b == c) or d):
                print(a, b, c, d)

    def f2_18(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if not (((z <= x) and (x <= w)) or (y == (z or x))):
                print(x, y, w, z)

    def f2_19(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if not ((x and z) or ((w <= x) == (z <= y))):
                print(x, y, w, z)

    def f2_20(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if not ((x == (not z)) <= ((x or w) == y)):
                print(x, y, w, z)


if __name__ == '__main__':
    homework = Homework2()
    homework.f2_17()
