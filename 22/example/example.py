def f22(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        my_list = []

        """Создание двумерного массива"""
        for s in file.readlines():
            number, time, need = s.split('\t')
            new_list = [int(number)] + [int(time)]
            new_list += [int(need.strip())] if need.strip() == '0' else [list(map(lambda el: int(el), need.replace(';', '').split()))]
            my_list.append(new_list)

        """Изменение двумерного массива"""
        for i in range(len(my_list)):
            number, time, need = my_list[i]
            if need == 0:
                my_list[i][2] = time
            else:
                max_time = max([my_list[i-1][2] for i in need]) + time
                my_list[i][2] = max_time

        max_value = max(my_list, key=lambda el: el[2])[2]

        return max_value


def main():
    filename = input('Your filename: ')
    result = f22(filename)
    print('Result: ', result)


if __name__ == '__main__':
    main()