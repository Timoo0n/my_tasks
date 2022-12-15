from itertools import product


def alg(s):
    while '31' in s or '32' in s:
        if '32' in s: s = s.replace('32', '3', 1)
        else: s = s.replace('31', '11', 1)
    return s
    

def main():
    print(len(list(filter(lambda el: el =='1', alg('31'*50+'2'*50)))))
        

if __name__ == '__main__': main()
