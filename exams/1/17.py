def f():
    with open('17.txt', 'r') as file:
        my_list = list(map(int, file.read().strip().split('\n')))

        min_value = 40

        count = 0
        min_list = []
        for i in range(1, len(my_list)):
            if my_list[i-1] % 40 == 0 and my_list[i] % 40 == 0:
                count += 1
                min_sum = min(sum(list(map(int, list(str(my_list[i-1]))))), sum(list(map(int, list(str(my_list[i]))))))
                print(max(my_list[i-1], my_list[i]))
                min_list += [min_sum]
        print(count, min_list)
        


if __name__ == '__main__': f()
