def f():
    with open('24.txt', 'r', encoding='utf-8') as file:
        my_str = file.read()
        while 'JBOSSJBOSSJ' in my_str:
            my_str.replace('JBOSSJBOSSJ', 'JBOSSJ JBOSSJ')

        return my_str.count('BOSS') - my_str.count('JBOSS') - my_str.count('BOSSJ') + my_str.count('JBOSSJ')


def main():
    print(f())


if __name__ == '__main__':
    main()