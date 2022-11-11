from itertools import product


class Homework2:
    def __init__(self):
        self.__my_list = product(range(2), repeat=4)
        self.__my_list1 = product(range(2), repeat=3)

    def f2_1(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if (x or (not y)) and (not (y == z)) and w:
                print(x, y, w, z)

    def f2_2(self):
        print('A B C F')
        for a, b, c in self.__my_list1:
            f = ((a and (not c)) or (not b) and (not c))*1
            print(a, b, c, f)

    def f2_3(self):
        print('X Y Z')
        for x, y, z in self.__my_list1:
            if ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z)):
                print(x, y, z)

    def f2_4(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if (((not x) and y) == z) and w:
                print(x, y, w, z)

    def f2_5(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if not ((x <= (y and (not z))) or w):
                print(x, y, w, z)

    def f2_6(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if not ((x and (not y)) or (x == z) or w):
                print(x, y, w, z)

    def f2_7(self):
        print('X Y Z')
        for x, y, z in self.__my_list1:
            if ((not x) and y and z) or (not x and not z):
                print(x, y, z)

    def f2_8(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if ((not y) and x and ((not z) or w)) == 1:
                print(x, y, w, z)

    def f2_9(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if (((not y) or x or z) and (z <= y)) == 0:
                print(x, y, w, z)

    def f2_10(self):
        print('X Y Z')
        for x, y, z in self.__my_list1:
            if (not (x == (y <= z))) == 1:
                print(x, y, z)

    def f2_11(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if not ((y <= x) or (not((x <= z) and (z <= x))) and (not w)):
                print(x, y, w, z)

    def f2_12(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if (not w) and ((y or z) <= ((not x) and y)):
                print(x, y, w, z)

    def f2_13(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if ((w <= y) or (not (y <= z))) and (not x) and (not (x == z)):
                print(x, y, w, z)

    def f2_14(self):
        print('X Y W Z')
        for x, y, w, z in self.__my_list:
            if not ((x <= y) or (not (w <= z))):
                print(x, y, w, z)

    def f2_15(self):
        print('A B C D')
        for a, b, c, d in self.__my_list:
            if (((a and b) == (not c)) and ((not b) or d)) == 1:
                print(a, b, c, d)

    def f2_16(self):
        print('X Y Z W')
        for x, y, z, w in self.__my_list:
            if not ((not (z and (not w))) or ((z <= w) == (x <= y))):
                print(x, y, z, w)

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
    homework.f2_8()
