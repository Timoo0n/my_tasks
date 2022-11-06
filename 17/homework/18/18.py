def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        new_list = []
        for i in range(1, len(my_list)):
            num1, num2 = my_list[i-1], my_list[i]
            if (num1 % 9 == 0 and num2 % 9 != 0 and num2 % 8 == 3) or (num1 % 9 != 0 and num2 % 9 == 0 and num1 % 8 == 3):
                new_list.append(max(num1, num2))

        return len(new_list), max(new_list)


if __name__ == '__main__':
    print(*f())