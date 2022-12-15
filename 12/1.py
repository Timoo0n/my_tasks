def f(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '2302', 1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201')
    return s
    

def main():
    for i1 in range(100):
        for i2 in range(100):
            for i3 in range(100):
                result = f('0' + '1'*i1 + '2'*i2 + '3'*i3)
                condition = result.count('1') == 51 and result.count('2') == 29 and result.count('3') == 23
                if condition: print(i3)



if __name__ == '__main__': main()
