def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        value = sum([int(i) for x in my_list if x % 35 == 0 for i in str(x)])
        new_list = []
        for i in range(1, len(my_list)):
            num1, num2 = my_list[i-1], my_list[i]
            if ((num1 > value) and (num2 <= value) and ((num2 % 16 == 15) and (num2 // 16 % 16 == 14))) or ((num2 > value) and (num1 <= value) and ((num1 % 16 == 15) and (num1 // 16 % 16 == 14))):
                new_list.append(num1+num2)
        return len(new_list), min(new_list)


if __name__ == '__main__':
    print(*f())