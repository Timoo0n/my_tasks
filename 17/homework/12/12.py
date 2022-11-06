def f():
    with open('17.txt') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        new_list = []
        for i in range(1, len(my_list)):
            num1, num2 = my_list[i-1], my_list[i]
            if (num1 + num2) >= 100 and (num1 < 0 or num2 < 0):
                new_list.append(num1*num2)

        return len(new_list), max(new_list)


if __name__ == '__main__':
    print(*f())