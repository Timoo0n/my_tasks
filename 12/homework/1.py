def alg(s):
    while '2222' in s or '8888' in s:
        if '2222' in s: s = s.replace('2222', '88', 1)
        else: s = s.replace('8888', '22', 1)
    return s


def main():
    print(alg('8'*70))


if __name__ == '__main__': main()
