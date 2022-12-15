def f(s):
    while '10' in s or '1' in s:
        if '10' in s:
            s = s.replace('10', '0001', 1)
        else:
            if '1' in s:
                s = s.replace('1', '0', 1)
    return s
    

def main():
    count = 0
    for i in range(1, 101):
        if len(f('1' + '0' * i)) % 7 == 0: count += 1
    print(count)


if __name__ == '__main__': main()
