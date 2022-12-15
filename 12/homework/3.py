def f(s):
    while '1' in s or '100' in s:
        if '100' in s: s = s.replace('100', '0001', 1)
        else: s = s.replace('1', '00', 1)
    return s


def main():
    result = f('1'+'0'*33)
    print(result.count('0'))


if __name__ == '__main__': main()
