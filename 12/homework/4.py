def alg(s):
    while '1111' in s:
        s = s.replace('1111', '2', 1)
        s = s.replace('222', '1', 1)
    return s


def main():
    result = alg('1'*46+'2'*31)
    print(result)


if __name__ == '__main__': main()
