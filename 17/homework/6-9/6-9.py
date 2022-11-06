class Homework17:
    def __init__(self):
        with open('17.txt') as file:
            self.__my_list = file.read().split()

    def f6(self):
        my_list = list(map(lambda el: int(el), self.__my_list))
        new_list = []
        for i in range(1, len(my_list)):
            num, num1 = my_list[i-1], my_list[i]
            if abs(num+num1) % 3 == 0 and abs(num+num1) % 6 != 0 and str(num*num1)[-1] == '8':
                new_list.append(num+num1)
        print(len(new_list), max(new_list))

    def f7(self):
        my_list = list(map(lambda el: int(el), self.__my_list))
        new_list = []
        for i in range(1, len(my_list)):
            num, num1 = my_list[i-1], my_list[i]
            if (num*num1) >= 0 and abs(num+num1) % 7 == 0:
                new_list.append(num*num1)
        print(len(new_list), min(new_list))

    def f8(self):
        my_list = list(map(lambda el: int(el), self.__my_list))
        new_list = []
        for i in range(len(my_list)-2):
            num, num1, num2 = my_list[i], my_list[i+1], my_list[i+2]
            if abs(num)*abs(num1)*abs(num2) % 7 == 0 and str(num+num1+num2)[-1] == '5':
                new_list.append(num+num1+num2)
        print(len(new_list), max(new_list))

    def f9(self):
        my_list = list(map(lambda el: int(el), self.__my_list))
        new_list = []
        for i in range(2, len(my_list)):
            if all(abs(my_list[i-j]) % 3 == 0 for j in range(3)) and any(abs(my_list[i-j]) % 12 == 0 for j in range(3)):
                new_list.append((my_list[i] + my_list[i-1] + my_list[i-2])/3)
        print(len(new_list), min(new_list))


if __name__ == '__main__':
    homework = Homework17()
    homework.f6()