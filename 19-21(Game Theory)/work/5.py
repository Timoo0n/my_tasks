def moves(x):
    #my_list = []
    #if (x+3) % 2 == 1: my_list.append(x+3)
    #if (x+1) % 2 == 1: my_list.append(x+1)
    #if (x*3) % 2 == 1: my_list.append(x*3)

    return (i for i in (x+1, x+3, x*3) if i % 2 == 1)


def f(h):
    if h >= 51: return 'WIN'
    elif any(f(i) == 'WIN' for i in moves(h)): return 'П1'
    elif all(f(i) == 'П1' for i in moves(h)): return 'В1'
    elif any(f(i) == 'В1' for i in moves(h)): return 'П2'
    elif all(f(i) == 'П1' or f(i) == 'П2' for i in moves(h)): return 'В2'


def main():
    for i in range(1, 51):
        result = f(i)
        if result == 'В2':
            print(i, result)


if __name__ == '__main__':
    main()

# 7
# 12 14
# 2