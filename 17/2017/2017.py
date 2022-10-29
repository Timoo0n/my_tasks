
def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))

        count = 0
        my_sum = 0
        for num in my_list:
            if num % 16 == 11 and num % 7 == 0 and num % 6 != 0 and num % 13 != 0 and num % 19 != 0:
                my_sum += num
                count += 1

        print(my_sum, count)


if __name__ == '__main__':
    f()