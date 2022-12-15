def alg(s):
    while '31' in s or '32' in s:
        if '32' in s: s = s.replace('32', '311')
        else: s = s.replace('31', '11')

    return s


def main():
    result1 = alg('31'*30+'2'*30)
    result2 = alg('32'*30+'1'*30)
    print(len(list(filter(lambda el: el == '1', result2))))


if __name__ == '__main__': main()
