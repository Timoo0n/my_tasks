def f():
    with open('17.txt') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        new_list = []
        count = 0
        for i in range(1, len(my_list)):
            num, num1 = my_list[i-1], my_list[i]
            if 50 <= (abs(num) + abs(num1)) <= 200:
                new_list += [num, num1]
                count += 1
        return count, min(new_list)


if __name__ == '__main__':
    print(f())