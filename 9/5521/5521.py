def read_file():
    with open('table.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: list(map(lambda el1: int(el1), el.split())), file.read().strip().split('\n')))
        return my_list


def task_condition():
    my_list_list = read_file()
    count = 0

    for my_list in my_list_list:
        my_dict = {i: my_list.count(i) for i in my_list}
        new_dict = my_dict
        if list(new_dict.values()).count(2) == 1:
            this_list = [i for i, y in new_dict.items() if y == 1]

            if len(this_list) == 4:
                average = sum(this_list)/len(this_list)
                my_sum = [i for i, y in new_dict.items() if y == 2][0] * 2

                if average <= my_sum:
                    count += 1

    return count


def main():
    print(task_condition())


if __name__ == '__main__':
    main()