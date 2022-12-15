def f(my_str):
    while '>1' in my_str or '>2' in my_str or '>3' in my_str:
        if '>1' in my_str:
            my_str = my_str.replace('>1', '22>3', 1)
        if '>2' in my_str:
            my_str = my_str.replace('>2', '2>', 1)
        if '>3' in my_str:
            my_str = my_str.replace('>3', '11>2', 1)

    return my_str


def main():
    result = f('>'+'2'*17+'3'*10+'1'*25)
    print(sum(list(map(int, list(result.replace('>', ''))))))


if __name__ == '__main__': main()
    
