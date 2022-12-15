def alg(s):
    while '25' in s or '355' in s or '4555' in s:
        if '25' in s: s = s.replace('25', '4', 1)
        elif '355' in s: s = s.replace('355', '2', 1)
        elif '4555' in s: s = s.replace('4555', '3')
    return s


def main():
    print(alg('2'+'5'*81))


if __name__ == '__main__': main()
