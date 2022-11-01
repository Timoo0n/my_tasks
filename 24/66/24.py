def f():
    with open('24.txt', 'r', encoding='utf-8') as file:
        my_str = file.read().replace('КОТ', '0').replace(' ', '')
        new_str, max_count = '', 0
        for sym in my_str:
            if sym == '0':
                new_str += sym
            else:
                max_count = max(max_count, len(new_str))
                new_str = ''

        return max_count


def main():
    print(f())


if __name__ == '__main__':
    main()
